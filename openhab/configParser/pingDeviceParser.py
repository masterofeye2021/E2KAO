from ast import List
import datetime

from openhab.configParser.mapping.networkMapping import NetworkMapping
from openhab.configParser.mapping.genericParser import GenericParser
from openhab.items.item_ import Item

from openhab.supportClasses.knxItemType import KnxItemType
from openhab.supportClasses.openhabBindingType import OpenhabBindingType
from openhab.supportClasses.openhabGroup import OpenhabGroup
from openhab.supportClasses.openhabBinding import OpenhabBinding
from openhab.supportClasses.openhabItemType import OpenhabItemType
from openhab.supportClasses.openhabOutputFormat import OpenhabOutputFormat
from openhab.supportClasses.openhabPhysicalUnit import OpenhabPhysicalUnit
from openhab.supportClasses.openhabTag import OpenhabTag
from openhab.supportClasses.fontAweSomeIcon import FontAweSomeIcon
from openhab.things.networkThing import NetworkThing

class PingDeviceParser(GenericParser):

    def __init__(self) -> None:
        self.sheet = None
        self.items: List[Item] = []
        self.things: List[NetworkThing] = []
        super().__init__()

    def loadSheet(self) -> None:
        # @todo magix number
        self.sheet = self.workbook["PING"]

    def readItems(self) -> None:
        for row in self.sheet.iter_rows(min_row=2, values_only=True):

            group = OpenhabGroup()
            group.addGroup(row[NetworkMapping.GROUP1])
            group.addGroup(row[NetworkMapping.GROUP2])
            group.addGroup(row[NetworkMapping.GROUP3])
            group.addGroup(row[NetworkMapping.GROUP4])

            self.items.append(Item(OpenhabItemType(row[NetworkMapping.TYPE]), "_".join(filter(bool, [
                row[NetworkMapping.LOCATION],
                row[NetworkMapping.ACCESS],
                row[NetworkMapping.NAME],
                row[NetworkMapping.EXTENTION]])).replace(" ", "_"),
                row[NetworkMapping.LABEL],
                FontAweSomeIcon(row[NetworkMapping.ICON]),
                group,
                OpenhabTag(row[NetworkMapping.TAG]),
                OpenhabPhysicalUnit(""),
                OpenhabOutputFormat(""),
                OpenhabBinding(OpenhabBindingType.PING_ONLINE),
                row[NetworkMapping.PERSISTENCE]
            ))

            self.items.append(Item(OpenhabItemType.DATETIME, "_".join(filter(bool, [
                row[NetworkMapping.LOCATION],
                row[NetworkMapping.ACCESS],
                row[NetworkMapping.NAME],
                row[NetworkMapping.EXTENTION],
                 "Last_Seen"])).replace(" ", "_"),
                row[NetworkMapping.LABEL],
                FontAweSomeIcon(row[NetworkMapping.ICON]),
                group,
                OpenhabTag(row[NetworkMapping.TAG]),
               OpenhabPhysicalUnit(""),
                OpenhabOutputFormat(""),
                OpenhabBinding(OpenhabBindingType.PING_LAST_SEEN),
                ""
            ))

        print(str(datetime.datetime.now()) + " - Network Items eingelesen.")

    def readThings(self) -> None:
        for row in self.sheet.iter_rows(min_row=2, values_only=True):

            type: str = row[NetworkMapping.TYPE].lower()

            self.things.append(NetworkThing(KnxItemType(type), "_".join(filter(bool, [
                row[NetworkMapping.LOCATION],
                row[NetworkMapping.ACCESS],
                row[NetworkMapping.NAME],
                row[NetworkMapping.EXTENTION]])).replace(" ", "_"),
                row[NetworkMapping.LABEL],
                row[NetworkMapping.MAC],
                row[NetworkMapping.IP],



            ))

        print(str(datetime.datetime.now()) + " - Network Things eingelesen.")
