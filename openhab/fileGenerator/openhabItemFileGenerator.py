from ast import List
from openhab.fileGenerator.fileGenerator import FileGenerator
from openhab.items.item_ import Item
from openhab.supportClasses.openhabItemType import OpenhabItemType


class OpenhabItemFileGenerator(FileGenerator):
    item_file_extention = ".items"
    item_file_deliminiter = " "

    def __init__(self, output_dir: str, file_name: str) -> None:
        super().__init__(output_dir, file_name)

    def generate(self, items) -> str:
        self.item_file = open(self.output_dir + "/" +
                              self.file_name + self.item_file_extention, "w",encoding="utf-8")

        # <type> <name> <label> <tag> <group> <
        for item in items:
            # Openhab Item Type <type>
            self.writeType(item)
            # Name des Items <name>
            self.writeName(item)
            # Label des Items <label>
            self.writeLabel(item)
            # Icon des Items <icon>
            self.writeIcon(item)
             # Zugeordnete Gruppen des Items <group>
            self.writeGroup(item)
            # Tags des Items <tag>
            self.writeTag(item)
            self.writeBindTo(item)
            #in die nächste Zeile springen
            self.item_file.write('\n')   
        self.item_file.close()

    def writeType(self, item: Item):
        self.item_file.write(item.type + self.item_file_deliminiter)

    def writeName(self, item: Item):
        self.item_file.write(item.name + self.item_file_deliminiter)

    def writeLabel(self, item: Item):
        self.item_file.write(item.label + self.item_file_deliminiter)

    def writeIcon(self, item: Item):
        self.item_file.write(item.icon + self.item_file_deliminiter)

    def writeGroup(self, item: Item):
        self.item_file.write(item.groups +
                             self.item_file_deliminiter)

    def writeTag(self, item: Item):
        self.item_file.write(item.tag + self.item_file_deliminiter)

    def writeBindTo(self, item: Item):
        if item.bound_to:
            if item.type == OpenhabItemType.DATETIME:
                 self.item_file.write("channel = \"ntp:ntp:local:dateTime\","  +item.bound_to + "[profile=“follow”]")
            else:
                self.item_file.write(item.bound_to)
        else:
            return
