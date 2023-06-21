from ast import List
import datetime
from openhab.fileGenerator.openhabThingFileGenerator import OpenhabThingFileGenerator
from openhab.things.knxThing import KnxThing
from openhab.things.thing import Thing


class KnxThingFileGenerator(OpenhabThingFileGenerator):
    def __init__(self, output_dir: str, file_name: str) -> None:
        super().__init__(output_dir, file_name)

    def generateAll(self, things) -> None:
        print(str(datetime.datetime.now()) + " - Erzeuge knx.things File.")
        self.generate()
        self.generateBride()
        self.generateDevice()
        for thing in things:
            self.generateDeviceElements(thing)
        self.item_file.write("\t"+"}"+"\n")
        self.item_file.write("}"+"\n")
        self.item_file.close()

        self.replaceUmlaute(self.item_file_extention)

        print(str(datetime.datetime.now()) + " - Knx Things File erzeugt.")

    def generateBride(self):
        self.item_file.write("Bridge knx:ip:bridge [" + "\n")
        self.item_file.write("\t"+ "type=\"TUNNEL\"," + "\n")
        self.item_file.write("\t"+"ipAddress=\"192.168.178.29\"," + "\n")
        self.item_file.write("\t"+"portNumber=3671,"+"\n")
        self.item_file.write("\t"+"localIp=\"192.168.178.42\","+"\n")
        self.item_file.write("\t"+"readingPause=50,"+"\n")
        self.item_file.write("\t"+"responseTimeout=10,"+"\n")
        self.item_file.write("\t"+"readRetriesLimit=3,"+"\n")
        self.item_file.write("\t"+"autoReconnectPeriod=60,"+"\n")
        self.item_file.write("\t"+"localSourceAddr=\"0.0.0\""+"\n")
        self.item_file.write("]{"+"\n")

    def generateDevice(self):
        self.item_file.write("\t"+"\t"+"Thing device generic ["+"\n")
        self.item_file.write("\t"+"\t"+"address=\"\","+"\n")
        self.item_file.write("\t"+"\t"+"fetch=true,"+"\n")
        self.item_file.write("\t"+"\t"+"pingInterval=300,"+"\n")
        self.item_file.write("\t"+"\t"+"readInterval=600"+"\n")
        self.item_file.write("] {"+"\n")

    def generateDeviceElements(self, thing: KnxThing):
        self.item_file.write("\t"+"\t"+"\t"+"Type ")
        self.item_file.write(
            thing.type + self.item_file_deliminiter + ":" + self.item_file_deliminiter + " ")
        self.item_file.write(thing.name+ " ")
        self.item_file.write("\"" + thing.label+ "\"" + " ")
        self.item_file.write(thing.group_adress +"\n")

