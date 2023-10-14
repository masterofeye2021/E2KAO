from ast import List
import datetime

from openhab.configParser.mapping.genericParser import GenericParser
from openhab.configParser.mapping.wetterMapping import WetterMapping
from openhab.items.item_ import Item
from openhab.supportClasses.openhabBindingType import OpenhabBindingType
from openhab.supportClasses.openhabGroup import OpenhabGroup
from openhab.supportClasses.openhabPhysicalUnit import OpenhabPhysicalUnit
from openhab.supportClasses.openhabOutputFormat import OpenhabOutputFormat
from openhab.supportClasses.openhabBinding import OpenhabBinding
from openhab.supportClasses.openhabItemType import OpenhabItemType
from openhab.supportClasses.openhabTag import OpenhabTag
from openhab.supportClasses.fontAweSomeIcon import FontAweSomeIcon
from openhab.things.knxThing import KnxThing
from openhab.things.wetterThing import WetterThing


class WetterParser(GenericParser):

    def __init__(self) -> None:
        self.sheet = None
        self.items: List[Item] = []
        self.things: List[WetterThing] = []


        super().__init__()

    def loadSheet(self) -> None:
        # @todo magix number
        self.sheet = self.workbook["WETTER"]

    def readItems(self) -> None:
        for row in self.sheet.iter_rows(min_row=2, values_only=True):

            group = OpenhabGroup()
            group.addGroup(row[WetterMapping.GROUP1])
            group.addGroup(row[WetterMapping.GROUP2])
            group.addGroup(row[WetterMapping.GROUP3])
            group.addGroup(row[WetterMapping.GROUP4])

            self.items.append(Item(OpenhabItemType(row[WetterMapping.TYPE]), "_".join(filter(bool, [
                row[WetterMapping.LOCATION],
                row[WetterMapping.ACCESS],
                row[WetterMapping.NAME],
                row[WetterMapping.EXTENTION],
                row[WetterMapping.FUNCTION]])).replace(" ", "_"),
                row[WetterMapping.LABEL],
                FontAweSomeIcon(row[WetterMapping.ICON]),
                group,
                OpenhabTag(row[WetterMapping.TAG]),
                OpenhabPhysicalUnit(row[WetterMapping.EINHEIT]),
                OpenhabOutputFormat(row[WetterMapping.FORMAT]),
                OpenhabBinding(OpenhabBindingType.WETTER).set_channelInfo(row[WetterMapping.CHANNEL]),
                row[WetterMapping.PERSISTENCE]
            ))

        print(str(datetime.datetime.now()) + " - Wetter Items eingelesen.")

    def readThings(self) -> None:
        for row in self.sheet.iter_rows(min_row=2, values_only=True):

            type: str = row[WetterMapping.TYPE].lower()

            group = KnxGroupAddress(row[WetterMapping.MAIN],  row[WetterMapping.MIDDLE],  row[WetterMapping.SUB],
                                    row[WetterMapping.MAIN2],  row[WetterMapping.MIDDLE2],  row[WetterMapping.SUB2],
                                    row[WetterMapping.MAIN3],  row[WetterMapping.MIDDLE3],  row[WetterMapping.SUB3], type, row[WetterMapping.DATENTYP])

            name = "_".join(filter(bool, [
                row[WetterMapping.LOCATION],
                row[WetterMapping.ACCESS],
                row[WetterMapping.NAME],
                row[WetterMapping.EXTENTION],
                row[WetterMapping.FUNCTION]])).replace(" ", "_")

            self.csv.write(name,row[WetterMapping.MAIN],  row[WetterMapping.MIDDLE],  row[WetterMapping.SUB])

            self.things.append(KnxThing(KnxItemType(type), name,
                row[WetterMapping.LABEL],
                group
                

            ))
        print(str(datetime.datetime.now()) + " - Network Things eingelesen.")
