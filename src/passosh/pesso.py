from dataclasses import dataclass
from app.fields import (HeaderField, PrimaryField, SecondaryField, BackField, AuxiliaryField, Barcode,
                        BoardingPassTransitType)

@dataclass
class Content:
    """
    An object that represents the groups of fields that display the information for an event ticket.
    """
    headerFields: list[HeaderField] | None = None
    primaryFields: list[PrimaryField] | None = None
    secondaryFields: list[SecondaryField] | None = None
    auxiliaryFields: list[AuxiliaryField] | None = None
    backFields: list[BackField] | None = None


@dataclass
class ContentBoardingPass(Content):
    transitType: BoardingPassTransitType = BoardingPassTransitType.AIR


@dataclass
class Passosh:
    organizationName: str
    passTypeIdentifier: str
    serialNumber: str
    teamIdentifier: str

    media: dict[str, bytes]

    barcodes: list[Barcode] = None

    eventTicket: Content | None = None
    generic: Content | None = None
    coupon: Content | None = None
    storeCard: Content | None = None
    boardingPass: ContentBoardingPass | None = None

    description: str | None = None
    foregroundColor: str | None = None
    labelColor: str | None = None

    formatVersion: int = 1
    suppressStripShine: bool = False
    voided: bool = False

    relevantDate: str | None = None
