from pathlib import Path

from app.fields import *
from app.pesso import Passosh, Content, ContentBoardingPass
from app.signature import create_pkpass

context = {
    "title": "[Passosh] Test autojoin v332",
    "description": "[Passosh] Test",
    "date": "13 DEC 18:00",
    "relevant_date": "2023-12-13T17:00:00+00:00",
    "expiration_date": "2023-12-14T17:00:00+00:00",
    "app_launch_url": "locals://test-autojoin-jdtu",
    "price": "0",
    "link": "https://web-app-dev.locals.org/test-autojoin-jdtu",
    "user": {
        "name": "Leha MCLAPA",
        "link": "https://web-app-dev.locals.org/@kripoha9999"
    },
    "host": {
        "name": "Kitty Sweety"
    },
    "address": "st. Vishnya 8, Warsaw",
    "serial_number": "v2_1a308de0-a1df-4837-8d14-41a44c211f4a",
    "meeting_place": "Vishnya, Warsaw, Poland"
}

ICONS_PATH = Path.cwd() / 'media'
dir_path = '/Users/mashihara/Downloads/assets/apple/'

def file_content(name: str, base_dir=ICONS_PATH) -> bytes:
    return open(ICONS_PATH / name, "rb").read()


def file_content_sign(name: str) -> bytes:
    return open(dir_path + name, 'rb').read()


def test_create_ticket():
    passosh = Passosh(
        organizationName="Locals",
        passTypeIdentifier="pass.org.locals.dev.wallet",
        teamIdentifier="UWND65J5RW",
        serialNumber=context['serial_number'],
        foregroundColor='#FFFFFF',
        labelColor='#FFFFFF',
        description=context['description'],
        media={
            'logo.png': file_content("logo.png"),
            'icon.png': file_content("icon.png"),
            'background.png': file_content("background.png"),
        },
        barcodes=[
            Barcode(
                message=context['user']['link'],
                format=BarcodeFormat.QR
            )
        ],
        eventTicket=Content(
            headerFields=[
                HeaderField(
                    key='meeting_date',
                    value=context['date'],
                    textAlignment=TextAlignment.RIGHT
                )
            ],
            primaryFields=[
                PrimaryField(
                    key='title',
                    value=context['title']
                )
            ],
            secondaryFields=[
                SecondaryField(
                    key='host',
                    value=context['host']['name'],
                    label='HOST'
                ),
                SecondaryField(
                    key='guest',
                    value=context['user']['name'],
                    label='GUEST',
                    textAlignment=TextAlignment.RIGHT.value,
                    changeMessage="Guest name changed: %@"
                ),
            ],
            auxiliaryFields=[
                AuxiliaryField(
                    key='meeting_place',
                    value=context['address'],
                    label='ADDRESS'
                )
            ],
            backFields=[
                BackField(
                    key='event_title',
                    value=context['title'],
                    label='Event'
                ),
                BackField(
                    key='description',
                    value=context['description'],
                    label='Description'
                ),
                WebLinkField(
                    key='event_url',
                    value=context['link'],
                    label='Event Page'
                ),
                BackField(
                    key='start_at',
                    value=context['date'],
                    label='Start'
                )
            ]
        )
    )

    # if context['meeting_place']:
    #     passosh.eventTicket.backFields.append(
    #         BackField(
    #             key='location',
    #             value=context['meeting_place'],
    #             label='Location'
    #         )
    #     )

    create_pkpass(
        passosh=passosh,
        filename="genetic_passosh.pkpass",
        sign=dict(
            cert_pem=file_content_sign('pass.org.locals.dev.wallet.pem'),
            key=file_content_sign('dw22.key'),
            password="ojeeC0af0Aezeeng2kei7cei6doeg6".encode("UTF-8"),
            wwdr=file_content_sign('wwdr.pem')
        )
    )
