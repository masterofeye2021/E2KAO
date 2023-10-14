
from openhab.supportClasses.fontAweSomeIcon import FontAweSomeIcon
from openhab.supportClasses.openhabBinding import OpenhabBinding
from openhab.supportClasses.openhabGroup import OpenhabGroup
from openhab.supportClasses.openhabOutputFormat import OpenhabOutputFormat
from openhab.supportClasses.openhabPhysicalUnit import OpenhabPhysicalUnit
from openhab.supportClasses.openhabItemType import OpenhabItemType
from openhab.supportClasses.openhabTag import OpenhabTag


class Item():
    '''
    @brief Kontruktor für die Erzeugung eines Openhabitems
    @param type Type des Items
    @param bound_to Optional da Gruppen keinen Channel haben denen sie zugeordnet werden können
    '''
    def __init__(self, type: OpenhabItemType,
                 name: str,
                 label: str,
                 icon: FontAweSomeIcon,
                 groups: OpenhabGroup,
                 tag: OpenhabTag,
                 unit: OpenhabPhysicalUnit = OpenhabPhysicalUnit(""),
                 state_format: OpenhabOutputFormat = OpenhabOutputFormat(""),
                 bound_to: OpenhabBinding = None,
                 persist: bool = False):

        self.type = type
        self._name = "i" + name.replace("#","_")
        self._label = label
        self.unit = unit
        self._state_format = state_format
        self._icon = icon
        self._groups = groups
        self._tag = tag
        self._bound_to = bound_to
        self.persist = persist
        

    @property
    def groups(self) -> str:
        return self._groups.toString()

    @groups.setter
    def groups(self, groups: OpenhabGroup):
        self._groups = groups

    @property
    def icon(self) -> str:
        return self._icon.toString()

    @icon.setter
    def icon(self, icon: FontAweSomeIcon):
        self._icon = icon

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name : str):
        self._name = name.strip()

    @property
    def state_format(self) -> str:
        return self._state_format.toString()

    @property
    def bound_to(self) -> str:
        return self._bound_to.toString(self)

    def bindingType(self):
        return self._bound_to.openhabItemType

    @property
    def label(self) -> str:
        if self.state_format and self.unit:
            return "\"" +  self._label  + " ["+ self.state_format + " " + self.unit + "]" + "\""
        else:
            return "\"" + self._label + "\""
    
    @property
    def tag(self) -> str:
        return self._tag.toString()