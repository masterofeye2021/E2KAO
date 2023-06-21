from ast import List
import datetime
from openhab.fileGenerator.openhabThingFileGenerator import OpenhabThingFileGenerator
from openhab.things.networkThing import NetworkThing



class PingDeviceThingFileGenerator(OpenhabThingFileGenerator):
    def __init__(self, output_dir: str, file_name: str) -> None:
        super().__init__(output_dir, file_name)

    def generateAll(self, things) -> None:
        print(str(datetime.datetime.now()) + " - Erzeuge ping.things File.")
        self.generate()
        
        for thing in things:
            self.generateDevice(thing)
        self.item_file.close()

        self.replaceUmlaute(self.item_file_extention)

        print(str(datetime.datetime.now()) + " - Ping Things File erzeugt.")

    def generateDevice(self,thing: NetworkThing):

        self.item_file.write("Thing network:pingdevice:"+thing.name+" [ hostname=\""+thing.ip+"\", macAddress=\""+thing.mac+"\" , retry=2, timeout=5000, refreshInterval=60000]"+"\n")




