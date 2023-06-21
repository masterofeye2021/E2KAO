from ast import List
import datetime
from openpyxl import Workbook
from knx.knx_csv import KnxCsvWritter

from openhab.configParser.mapping.knxMapping import KnxMapping
from openhab.configParser.genericParser import GenericParser
from openhab.items.item_ import Item
from openhab.supportClasses.knxGroupAddress import KnxGroupAddress
from openhab.supportClasses.knxItemType import KnxItemType
from openhab.supportClasses.openhabBindingType import OpenhabBindingType
from openhab.supportClasses.openhabGroup import OpenhabGroup
from openhab.supportClasses.openhabPhysicalUnit import OpenhabPhysicalUnit
from openhab.supportClasses.openhabOutputFormat import OpenhabOutputFormat
from openhab.supportClasses.openhabBinding import OpenhabBinding
from openhab.supportClasses.openhabItemType import OpenhabItemType
from openhab.supportClasses.openhabTag import OpenhabTag
from openhab.supportClasses.fontAweSomeIcon import FontAweSomeIcon
from openhab.things.knxThing import KnxThing


class KnxParser(GenericParser):

    def __init__(self) -> None:
        self.sheet = None
        self.items: List[Item] = []
        self.things: List[KnxThing] = []

        self.csv = KnxCsvWritter()


        super().__init__()

    def loadSheet(self) -> None:
        # @todo magix number
        self.sheet = self.workbook["KNX"]

    def readItems(self) -> None:
        for row in self.sheet.iter_rows(min_row=2, values_only=True):

            group = OpenhabGroup()
            group.addGroup(row[KnxMapping.GROUP1])
            group.addGroup(row[KnxMapping.GROUP2])
            group.addGroup(row[KnxMapping.GROUP3])
            group.addGroup(row[KnxMapping.GROUP4])

            self.items.append(Item(OpenhabItemType(row[KnxMapping.TYPE]), "_".join(filter(bool, [
                row[KnxMapping.LOCATION],
                row[KnxMapping.ACCESS],
                row[KnxMapping.NAME],
                row[KnxMapping.EXTENTION],
                row[KnxMapping.FUNCTION]])).replace(" ", "_"),
                row[KnxMapping.LABEL],
                FontAweSomeIcon(row[KnxMapping.ICON]),
                group,
                OpenhabTag(row[KnxMapping.TAG]),
                OpenhabPhysicalUnit(row[KnxMapping.EINHEIT]),
                OpenhabOutputFormat(""),
                OpenhabBinding(OpenhabBindingType.KNX),
                row[KnxMapping.PERSISTENCE]
            ))

        print(str(datetime.datetime.now()) + " - KNX Items eingelesen.")

    def readThings(self) -> None:
        for row in self.sheet.iter_rows(min_row=2, values_only=True):

            type: str = row[KnxMapping.TYPE].lower()

            group = KnxGroupAddress(row[KnxMapping.MAIN],  row[KnxMapping.MIDDLE],  row[KnxMapping.SUB],
                                    row[KnxMapping.MAIN2],  row[KnxMapping.MIDDLE2],  row[KnxMapping.SUB2],
                                    row[KnxMapping.MAIN3],  row[KnxMapping.MIDDLE3],  row[KnxMapping.SUB3], type, row[KnxMapping.DATENTYP])

            name = "_".join(filter(bool, [
                row[KnxMapping.LOCATION],
                row[KnxMapping.ACCESS],
                row[KnxMapping.NAME],
                row[KnxMapping.EXTENTION],
                row[KnxMapping.FUNCTION]])).replace(" ", "_")

            self.csv.write(name,row[KnxMapping.MAIN],  row[KnxMapping.MIDDLE],  row[KnxMapping.SUB])

            self.things.append(KnxThing(KnxItemType(type), name,
                row[KnxMapping.LABEL],
                group
                

            ))
        print(str(datetime.datetime.now()) + " - Network Things eingelesen.")
