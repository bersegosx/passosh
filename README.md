# Passosh
Generate passes (.pkpass) files for Apple Wallet


## Install

```shell
pip install passosh
```

## Usage

```python
from passosh.fields import *
from passosh.pesso import Passosh, Content
from passosh.signature import create_pkpass


passosh = Passosh(
    organizationName="<Your org>",
    passTypeIdentifier="pass.your.org",
    teamIdentifier="XXXXX",
    serialNumber="YYYYYYYYYY",
    foregroundColor='#FFFFFF',
    labelColor='#FFFFFF',
    media={
        'icon.png': open("icon.png", 'rb').read(),
        'icon@2x.png': open("icon@2x.png", 'rb').read(),
        'logo.png': open("logo.png", 'rb').read(),
        'background.png': open("background.png", 'rb').read(),
    },
    barcodes=[
        Barcode(
            message="https://google.com",
            format=BarcodeFormat.QR
        )
    ],
    eventTicket=Content(
        headerFields=[
            HeaderField(
                key='date',
                value='19/12/23',
                textAlignment=TextAlignment.RIGHT,
                changeMessage='changed: %d'
            )
        ],
        primaryFields=[
            PrimaryField(
                key='title',
                value='Title here'
            )
        ],
        secondaryFields=[
            SecondaryField(
                key='place',
                value='Yatta Ramen BBQ, Warsaw',
                label='PLACE'
            ),
            SecondaryField(
                key='user',
                value='Nikola Teslovich',
                label='GUEST',
                textAlignment=TextAlignment.RIGHT.value,
                changeMessage="Guest name is changed: %@"
            ),
        ],
    ),
)

create_pkpass(
    passosh=passosh,
    filename="you_filename.pkpass",
    sign=dict(
        cert_pem=b'<pem cert content>',
        key=b'<key content'>,
        password=b'<key\'s password>',
        wwdr=b'<wwdr cet content>'
    )
)

```
