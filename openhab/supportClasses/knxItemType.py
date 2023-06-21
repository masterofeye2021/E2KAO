from strenum import StrEnum


class KnxItemType(StrEnum):
    SWITCH = "switch",
    CONTACT = "contact",
    NUMBER = "number",
    DATETIME = "datetime",
    DIMMER = "dimmer",
    ROLLERSHUTTER = "rollershutter",
    STRING = "string",
    DATETIME_CONTROL = "datetime-control",
    SWITCH_CONTROL = "switch-control",
    ROLLERSHUTTER_CONTROL = "rollershutter-control",
    CONTACT_CONTROL = "contact-control"

