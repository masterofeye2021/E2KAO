from openhab.supportClasses.knxGroupAddress import KnxGroupAddress
from openhab.supportClasses.knxItemType import KnxItemType
from openhab.things.thing import Thing


class KnxThing(Thing):
    def __init__(self, type: KnxItemType, name: str,  label: str, group_address:KnxGroupAddress) -> None:
        self.type = type
        self.label = label
        self._group_adress = group_address
        super().__init__(name)

    @property
    def group_adress(self) -> str:
        return self._group_adress.toString()
