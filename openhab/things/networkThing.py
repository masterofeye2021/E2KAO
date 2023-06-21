
from openhab.supportClasses.knxItemType import KnxItemType
from openhab.things.thing import Thing


class NetworkThing(Thing):
    def __init__(self, type: KnxItemType, name: str,  label: str, mac : str, ip : str) -> None:
        self.type = type
        self.label = label
        self.mac = mac
        self.ip = ip
        super().__init__(name)
