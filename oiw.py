#Diese Klasse ist der Openhab Item Writer (kirz oiw)

from openpyxl import load_workbook
from openhab.openhab_equipment import OpenhabEquipment
from openhab.openhab_item import ItemName, OpenhabItem

class OpenhabItemWritter:
    def __init__(self) -> None:
        self.file = "export/knx_generated.items"
        self.pid = None
        self.delimiter = " "
    
    def write_items(self, list_of_equipment, list_of_items):
        #File öffnen
        self.pid = open(self.file, 'w',encoding="utf-8")
        
        equipment : OpenhabEquipment
        for equipment in list_of_equipment:
            self.write_equipment(equipment)
            item : OpenhabItem
            for item in list_of_items : 
                if(item.equipment in equipment.name.get_name("l")):
                    item.add_group(equipment.name.get_name("e"))
                    self.write_item(item)

        self.pid.close()

    def write_equipment(self, openhabequipment : OpenhabEquipment):
        self.pid.write("\n")
        self.__write_type("Group")  
        self.__write_name(openhabequipment.name,"e")  
        self.__write_label(openhabequipment.label,"","")
        self.__write_icon(openhabequipment.icon)
        self.__write_group(openhabequipment.group)
        self.__write_tag("Equipment")

        #Itemdefintion abgeschlossen. Das nächste Item startet in der nächsten Zeile
        self.pid.write("\n")
        self.pid.write("\n")


    def write_item(self, openhabitem : OpenhabItem):
        self.__write_type(openhabitem.type)
        self.__write_name(openhabitem.name)
        self.__write_label(openhabitem.label, openhabitem.format, openhabitem.einheit)
        self.__write_icon(openhabitem.icon)
        self.__write_group(openhabitem.group)
        self.__write_tag(openhabitem.tag)
        self.__write_bound_to(openhabitem.bound_to)

        #Itemdefintion abgeschlossen. Das nächste Item startet in der nächsten Zeile
        self.pid.write("\n")

    def __write_type(self, type : str):
        self.pid.write(type.strip())
        self.pid.write(self.delimiter)
    
    def __write_name(self, name : ItemName, prefix : str = "i"):
        self.pid.write(name.get_name(prefix).strip().replace(" ","_"))
        self.pid.write(self.delimiter)

    def __write_label(self, label : str, format : str, einheit : str):
        if label: 
            self.pid.write("\""+ label.strip())
        else:
            raise ValueError("Label nicht gesetzt")

        if format and einheit:
            self.pid.write( " [" + format.strip())
            self.pid.write(self.delimiter)
            self.pid.write( einheit.strip() + "]")

        if label:
            self.pid.write("\"") 
            self.pid.write(self.delimiter) 

    def __write_icon(self, icon : str):
        if icon:
            self.pid.write("<ik" + icon.strip() + ">")
            self.pid.write(self.delimiter)
    
    def __write_group(self, group : str):
        if group:
            self.pid.write("(" + group.strip() + ")")
            self.pid.write(self.delimiter)

    def __write_tag(self, tag : str):
        if tag:
            self.pid.write("[\"" + tag.strip() + "\"]")
            self.pid.write(self.delimiter)

    def __write_bound_to(self, bound_to : str):
        if bound_to:
            self.pid.write(bound_to.strip())
            self.pid.write(self.delimiter)


      
