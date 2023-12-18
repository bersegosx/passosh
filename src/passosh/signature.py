import hashlib
import json
from dataclasses import asdict

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.serialization import pkcs7

from app.pesso import Passosh
from app.zip import write_zip


def create_pass_data(passosh: Passosh) -> dict:
    result = asdict(passosh)
    del result['media']

    for k, v in result.copy().items():
        if v is None:
            del result[k]

    return result


def get_sha1(content: bytes) -> str:
    return hashlib.sha1(content).hexdigest()


def create_manifest(files: dict[str, bytes]) -> dict[str, str]:
    return {
        filename: get_sha1(content)
        for filename, content in files.items()
    }


def create_signature(manifest: dict, cert_pem: bytes, key: bytes, password: bytes, wwdr: bytes) -> bytes:
    # cert in pem, output in der

    cert = x509.load_pem_x509_certificate(cert_pem)
    cert_key = serialization.load_pem_private_key(
        key,
        password=password
    )
    wwdr_cert = x509.load_pem_x509_certificate(wwdr)

    manifest_data = json.dumps(manifest).encode()
    return (
        pkcs7.PKCS7SignatureBuilder()
        .set_data(manifest_data)
        .add_signer(cert, cert_key, hashes.SHA256())
        .add_certificate(wwdr_cert)
        .sign(serialization.Encoding.DER, [pkcs7.PKCS7Options.DetachedSignature])
    )


def create_pkpass(passosh: Passosh, filename: str, sign: dict):
    pass_data: dict = create_pass_data(passosh)
    pass_content = json.dumps(pass_data).encode()

    manifest_files = passosh.media | {"pass.json": pass_content}
    manifest: dict = create_manifest(manifest_files)

    signature: bytes = create_signature(
        manifest=manifest,
        cert_pem=sign['cert_pem'],
        key=sign['key'],
        password=sign['password'],
        wwdr=sign['wwdr']
    )

    files = manifest_files | {
        "manifest.json": json.dumps(manifest).encode(),
        "signature": signature
    }

    write_zip(filename, files)
