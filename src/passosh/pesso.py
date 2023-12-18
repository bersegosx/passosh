from dataclasses import dataclass

from .fields import (HeaderField, PrimaryField, SecondaryField, BackField, AuxiliaryField, Barcode,
                     BoardingPassTransitType, Location)


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
    locations: list[Location] = None

    eventTicket: Content | None = None
    generic: Content | None = None
    coupon: Content | None = None
    storeCard: Content | None = None
    boardingPass: ContentBoardingPass | None = None

    backgroundColor: str | None = None  # CSS-style RGB triple, ex: "rgb(0, 185, 255)"
    foregroundColor: str | None = None
    labelColor: str | None = None

    formatVersion: int = 1
    suppressStripShine: bool = False
    voided: bool = False

    # The maximum distance, in meters, from a location in the locations array at which the pass is relevant.
    # The system uses the smaller of either this distance or the default distance.
    maxDistance: int | None = None

    relevantDate: str | None = None
    expirationDate: str | None = None

    # controls whether to show the Share button on the back of a pass.
    # A value of true removes the button.
    sharingProhibited: bool = False

    logoText: str | None = None
    description: str | None = None
    appLaunchURL: str | None = None
    associatedStoreIdentifiers: list[str] | None = None

    authenticationToken: str | None = None
    webServiceURL: str | None = None

    # TODO: add types
    semantics = None
    userInfo: dict | None = None
