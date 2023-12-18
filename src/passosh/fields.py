import dataclasses
from dataclasses import dataclass
from enum import Enum, unique


@unique
class TextAlignment(str, Enum):
    """
    The alignment for the content of a field.
    The default is natural alignment, which aligns the text based on its script direction.

    This key is invalid for primary and back fields.
    """

    NATURAL = 'PKTextAlignmentNatural'
    LEFT = 'PKTextAlignmentLeft'
    RIGHT = 'PKTextAlignmentRight'
    CENTER = 'PKTextAlignmentCenter'


@dataclass
class HeaderField:
    """
    An object that represents the fields that display information at the top of a pass.
    """
    key: str
    value: str
    label: str = ''
    textAlignment: str = TextAlignment.NATURAL

    changeMessage: str = ''


@dataclass
class PrimaryField:
    """
    An object that represents the fields that display the most important information on a pass.
    """
    key: str
    value: str
    label: str = ''

    changeMessage: str = ''


@dataclass
class SecondaryField:
    """
    An object that represents the fields that display supporting information on the front of a pass.
    """
    key: str
    value: str
    label: str = ''
    textAlignment: str = TextAlignment.NATURAL

    changeMessage: str = ''


@dataclass
class AuxiliaryField:
    """
    An object that represents the fields that display additional information on the front of a pass.
    """
    key: str
    value: str
    label: str = ''
    textAlignment: str = TextAlignment.NATURAL

    changeMessage: str = ''
    row: int = 0


@dataclass
class BackField:
    """
    An object that represents the fields that display information on the back of a pass.
    """
    key: str
    value: str
    label: str = ''

    changeMessage: str = ''


@dataclass
class WebLinkField:
    """
    The value of the field, including HTML markup for links.
    The only supported tag is the <a> tag and its href attribute.
    The value of this key overrides that of the value key.

    The attributed value isn’t used for watchOS; use the value field instead.
    """
    key: str
    value: str

    label: str = ''
    attributedValue: str = dataclasses.field(init=False)

    def __post_init__(self):
        self.attributedValue = f"<a href='{self.value}'>{self.value}</a>"


@unique
class BarcodeFormat(str, Enum):
    """
    The format of the barcode
    """
    QR = 'PKBarcodeFormatQR'
    PDF417 = 'PKBarcodeFormatPDF417'
    AZTEC = 'PKBarcodeFormatAztec'
    CODE128 = 'PKBarcodeFormatCode128'  # isn’t supported for watchOS


@dataclass
class Barcode:
    message: str
    format: BarcodeFormat
    messageEncoding: str = 'iso-8859-1'

    altText: str = ''   # isn’t displayed for watchOS


@unique
class BoardingPassTransitType(str, Enum):
    GENERIC = 'PKTransitTypeGeneric'
    AIR = 'PKTransitTypeAir'
    BOAT =  'PKTransitTypeBoat'
    BUS = 'PKTransitTypeBus'
    TRAIN = 'PKTransitTypeTrain'


@dataclass
class Location:
    """
    An object that represents a location that the system uses to show a relevant pass.
    """
    latitude: float  # in degrees, of the location
    longitude: float  # in degrees, of the location
    altitude: float | None = None  # in meters, of the location

    # the text to display on the lock screen when the pass is relevant.
    # For example, a description of a nearby location, such as “Store nearby on 1st and Main”.
    relevantText: str | None = None
