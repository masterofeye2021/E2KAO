import json
from openpyxl import load_workbook
from knx.group_address import GroupAddress
import item_mapping
import equipment_mapping
from knx.knx_csv import KnxCsvWritter
from oiw import OpenhabItem, OpenhabItemWritter
from openhab.openhab_channel import OpenhabChannel
from openhab.openhab_equipment import OpenhabEquipment
from openhab.openhab_generic import OpenhabGeneric
from openhab.openhab_item import ItemName
import api_caller
import time

sheet_name_point : str = "KNX"
sheet_name_equipment : str = "Equipment"


def xls2item(path :str):
   items = []
   euipments = []
   workbook = load_workbook(filename="source/knx.xlsx", data_only=True)
   sheet = workbook[sheet_name_point]

   #Thing von Openhab Instance abrufen
   uid = api_caller.get_knx_device_uid()
   uid_hex_value = api_caller.get_uid_hex_value(uid)
   thing = api_caller.get_thing_by_uid(uid)

   kcw = KnxCsvWritter()

   for row in sheet.iter_rows(min_row=2, values_only=True):

      iten_name = ItemName(row[item_mapping.PREFIX1], row[item_mapping.PREFIX2], row[item_mapping.NAME], row[item_mapping.SUFFIX1], row[item_mapping.SUFFIX2],"i")      
      
      oi = OpenhabItem(row[item_mapping.TYPE],
                        iten_name,
                        row[item_mapping.LABEL],
                        row[item_mapping.FORMAT],
                        row[item_mapping.EINHEIT],
                        OpenhabGeneric.__set_group__(
                           row[item_mapping.GROUP1],
                           row[item_mapping.GROUP2],
                           row[item_mapping.GROUP3],
                           row[item_mapping.GROUP4]),
                        row[item_mapping.ICON],
                        row[item_mapping.TAG],
                        row[item_mapping.BOUND_TO],
                        row[item_mapping.EQUIPMENT],           
                        )

      group_address = []
      group_address.append(GroupAddress(row[item_mapping.MAIN],row[item_mapping.MIDDLE],row[item_mapping.SUB]))
      group_address.append(GroupAddress(row[item_mapping.MAIN2],row[item_mapping.MIDDLE2],row[item_mapping.SUB2]))
      group_address.append(GroupAddress(row[item_mapping.MAIN3],row[item_mapping.MIDDLE3],row[item_mapping.SUB3]))

      kcw.write(oi.name.get_name("ga"), group_address[0].main, group_address[0].middle, group_address[0].sub)

      #Nun sind wir in der Lage ein Channel zu erzeugen 
      channel : OpenhabChannel =  OpenhabChannel(uid,
                                          uid_hex_value,
                                          iten_name.get_name("c"),
                                          row[item_mapping.TYPE],
                                          row[item_mapping.TYPE],
                                          row[item_mapping.LABEL],
                                          group_address = group_address)

      oi.__set_bound_to__(channel.uid,row[item_mapping.TRANSFORM])                                    
      #Channel in Json umwandeln, um ihn dem Thing Objekt hinzuzufügen
      channel_json = json.loads(channel.json())
      thing["channels"].append(channel_json)

      items.append(oi)
   
   #Euipment Liste wird erstellt
   sheet = workbook[sheet_name_equipment]
   for row in sheet.iter_rows(min_row=2, values_only=True):
      oe = OpenhabEquipment(ItemName.create_by_name(row[equipment_mapping.NAME]),row[equipment_mapping.LABEL],
                  row[equipment_mapping.ICON],
                  row[equipment_mapping.LOCALATION],
                  OpenhabGeneric.__set_group__(
                           row[equipment_mapping.GROUP1],
                           row[equipment_mapping.GROUP2],
                           row[equipment_mapping.GROUP3],
                           row[equipment_mapping.GROUP4]))
      euipments.append(oe)

   kcw.close()
   #Schreiben der Liste an erzeugen Items
   writter = OpenhabItemWritter()
   writter.write_items(euipments, items)

   api_caller.delete_channels(uid,OpenhabGeneric.__remove_umlaut__(json.dumps(thing,ensure_ascii=False)))
   time.sleep(5)
   api_caller.change_thing(uid,OpenhabGeneric.__remove_umlaut__(json.dumps(thing,ensure_ascii=False)))
  


