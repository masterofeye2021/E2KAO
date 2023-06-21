from ast import List
import datetime
from openhab.fileGenerator.openhabItemFileGenerator import OpenhabItemFileGenerator


class PvModbusItemFileGenerator(OpenhabItemFileGenerator):
    def __init__(self, output_dir: str, file_name: str) -> None:
        super().__init__(output_dir, file_name)

    def generate(self, items) -> str:
        print(str(datetime.datetime.now()) + " - Erzeuge Modbus .items File.")
        
        super().generate(items)

        self.replaceUmlaute(self.item_file_extention)

        print(str(datetime.datetime.now()) + " - Modbus Item File erzeugt.")