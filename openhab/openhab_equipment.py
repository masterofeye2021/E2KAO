
import dataclasses
from openhab.openhab_generic import OpenhabGeneric
from openhab.openhab_item import ItemName


@dataclasses.dataclass
class OpenhabEquipment:
    name : ItemName
    label : str
    icon : str
    location : str
    group : str

    def __post_init__(self):
        self.icon =  OpenhabGeneric.__remove_umlaut__(self.icon)
        self.location =  OpenhabGeneric.__remove_umlaut__(self.location)
        self.group =  OpenhabGeneric.__remove_umlaut__(self.group)