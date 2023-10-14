from strenum import StrEnum

class OpenhabItemType(StrEnum):
    SWITCH = "Switch",
    NUMBER = "Number",
    NUMBER_TEMPERATURE = "Number:Temperature",
    NUMBER_PRESSURE = "Number:Pressure",
    NUMBER_DIMENSIONLESS = "Number:Dimensionless",
    NUMBER_SPEED = "Number:Speed",
    NUMBER_ANGLE = "Number:Angle",
    NUMBER_LENGTH = "Number:Length",
    COLOR = "Color",
    CONTACT = "Contact",
    DATETIME = "DateTime",
    DIMMER = "Dimmer",
    GROUP = "Group",
    IMAGE = "Image",
    LOCATION = "Locatiom",
    ROLLERSHUTTER = "Rollershutter",
    STRING = "String",
    DATETIME_CONTROL = "datetime-control",
    SWITCH_CONTROL = "switch-control"
