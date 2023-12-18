from zipfile import ZipFile


def write_zip(file_obj, files: dict[str, bytes]):
    with ZipFile(file_obj, 'w') as zipf:
        for fname, data in files.items():
            zipf.writestr(fname, data)
