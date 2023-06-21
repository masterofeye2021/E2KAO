from ast import List
import datetime
from openhab.fileGenerator.openhabThingFileGenerator import OpenhabThingFileGenerator
from openhab.things.knxThing import KnxThing
from openhab.things.modbusPoller import ModbusPoller
from openhab.things.modbusThing import ModbusThing


class PvModbusThingFileGenerator(OpenhabThingFileGenerator):
    def __init__(self, output_dir: str, file_name: str) -> None:
        super().__init__(output_dir, file_name)

    def generateAll(self, things, poller) -> None:
        print(str(datetime.datetime.now()) +
              " - Erzeuge ModbusPV.things File.")
        self.generate()
        self.generateBrideTCP("Photovoltaik Modbus TCP Slave",
                              "192.168.178.33", 502, 1, 1500,poller,things)

        self.item_file.close()

        self.replaceUmlaute(self.item_file_extention)

        print(str(datetime.datetime.now()) +
              " - ModbusPV Things File erzeugt.")

    def generateBrideTCP(self, label: str, host: str, port: int, id: int, timeBetweenTransactionsMillis: int, pollers, things):
        self.item_file.write("Bridge modbus:tcp:pv \"" + label + "\" [ host=\"" + host + "\", port=" + str(port) + ", id=" + str(id) + ", timeBetweenTransactionsMillis=" + str(timeBetweenTransactionsMillis) + " ] {" + "\n")
        
        #generate the modbus poller
        for poller in pollers:
            self.generatePoller(poller,things)

        #close the bridge definition
        self.item_file.write("}"+"\n")

    def generateBrideSerial(self):
        raise Exception("Not Implemented")

    def generatePoller(self, poller: ModbusPoller, things):
        self.item_file.write("\t"+"\t"+"Bridge poller " + poller.name + " \"" + poller.label +"\" [ start=" + str(poller.adress) + ", length=" + str(poller.lenth)+  ", refresh=" + str(500) + ", type=\""+ poller.type + "\"" + "]"+ "{" +"\n")
        for thing in things:
            if thing.poller == poller.id:
                self.generateDeviceElements(thing)
        self.item_file.write("\n"+"\t"+"\t"+"}"+"\n")

    def generateDeviceElements(self, thing: ModbusThing):
        self.item_file.write("\t"+"\t"+"\t"+"Thing data ")
        self.item_file.write(thing.name + " ")
        self.item_file.write("\"" + thing.label + "\"" )
        self.item_file.write(" [ readStart=\""+ str(thing.adress)+"\", readValueType=\""+ thing.type+"\" ]"+  "\n")

