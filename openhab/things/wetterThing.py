from openhab.supportClasses.knxGroupAddress import KnxGroupAddress
from openhab.supportClasses.knxItemType import KnxItemType
from openhab.things.thing import Thing


class WetterThing(Thing):
    def __init__(self,name: str,  label: str, address : str, length : str, type: str, id: int) -> None:
        self.label = label
        self.adress = address
        self.lenth = length
        self.type = type
        self.id = id
        super().__init__(name)
