from strenum import StrEnum

class OpenhabItemType(StrEnum):
    SWITCH = "Switch",
    NUMBER = "Number",
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
