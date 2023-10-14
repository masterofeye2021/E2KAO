
from knx.knx_csv import KnxCsvWritter
from openhab.configParser.knxParster import KnxParser
from openhab.configParser.modbusParser import ModbusParser
from openhab.configParser.pingDeviceParser import PingDeviceParser
from openhab.configParser.serviceDeviceParser import ServiceDeviceParser
from openhab.configParser.wetterParser import WetterParser
from openhab.fileGenerator.knxItemFileGenerator import KnxItemFileGenerator
from openhab.fileGenerator.knxThingFileGenerator import KnxThingFileGenerator
from openhab.fileGenerator.pingDeviceItemFileGenerator import \
    PingDeviceItemFileGenerator
from openhab.fileGenerator.pingDeviceThingFileGenerator import \
    PingDeviceThingFileGenerator
from openhab.fileGenerator.pvModbusItemFileGenerator import \
    PvModbusItemFileGenerator
from openhab.fileGenerator.pvModbusThingFileGenerator import \
    PvModbusThingFileGenerator
from openhab.fileGenerator.serviceDeviceItemFileGenerator import \
    ServiceDeviceItemFileGenerator
from openhab.fileGenerator.serviceDeviceThingFileGenerator import \
    ServiceDeviceThingFileGenerator
from openhab.fileGenerator.wetterItemFileGenerator import WetterItemFileGenerator

sheet_name_point : str = "KNX"
sheet_name_equipment : str = "Equipment"

def xls2item(path :str):
   knx = KnxParser()
   knx.loadWorkbook()
   knx.loadSheet()
   knx.readItems()
   knx.readThings()


   ping  = PingDeviceParser()
   ping.loadWorkbook()
   ping.loadSheet()
   ping.readItems()
   ping.readThings()

   service = ServiceDeviceParser()
   service.loadWorkbook()
   service.loadSheet()
   service.readItems()
   service.readThings()

   modbus = ModbusParser()
   modbus.loadWorkbook()
   modbus.loadSheet()
   modbus.readItems()
   modbus.readThings()
   modbus.readPoller()

   wetter = WetterParser()
   wetter.loadWorkbook()
   wetter.loadSheet()
   wetter.readItems()
   #modbus.readThings()


   

   knxFilegenerator = KnxItemFileGenerator("export","knx")
   knxFilegenerator.generate(knx.items)
   
   knxThingFileGenerator = KnxThingFileGenerator("export","knx")
   knxThingFileGenerator.generateAll(knx.things)

   pingDeviceItemFileGenerator = PingDeviceItemFileGenerator("export","ping")
   pingDeviceItemFileGenerator.generate(ping.items)

   pingDeviceThingFileGenerator = PingDeviceThingFileGenerator("export","ping")
   pingDeviceThingFileGenerator.generateAll(ping.things)
   
   serviceDeviceItemFileGenerator = ServiceDeviceItemFileGenerator("export","service")
   serviceDeviceItemFileGenerator.generate(service.items)

   serviceDeviceThingFileGenerator = ServiceDeviceThingFileGenerator("export","service")
   serviceDeviceThingFileGenerator.generateAll(service.things)

   modbusItemFileGenerator = PvModbusItemFileGenerator("export","modbus")
   modbusItemFileGenerator.generate(modbus.items)

   modbusThingFileGenerator =  PvModbusThingFileGenerator("export","modbus")
   modbusThingFileGenerator.generateAll(modbus.things,modbus.poller) 

   wetterItemFileGenerator =  WetterItemFileGenerator("export","wetter")
   wetterItemFileGenerator.generate(wetter.items)   
      
   
