
import dataclasses
from openhab.openhab_item import ItemName


@dataclasses.dataclass
class OpenhabEquipment:
    name : ItemName
    label : str
    icon : str
    location : str
    group : str