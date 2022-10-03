#Diese Klasse ist der Openhab Item Writer (kirz oiw)

from openpyxl import load_workbook
from openhab.equipment.equipment import Equipment
from openhab.items.item import OpenhabItem
from openhab.items.knx_item import KnxItem

class OpenhabItemWritter:
    def __init__(self) -> None:
        self.file = "export/knx_generated.items"
        self.pid = None
        self.delimiter = " "
    
    def write_items(self, list_of_equipment, list_of_items):
        #File öffnen
        self.pid = open(self.file, 'w',encoding="utf-8")
        
        equipment : Equipment
        for equipment in list_of_equipment:
            self.write_equipment(equipment)
            item : OpenhabItem
            for item in list_of_items : 
                if(item.equipment in equipment.name):
                    item.add_group(equipment.name)
                    self.write_item(item)

        self.pid.close()

    def write_equipment(self, equipment : Equipment):
        self.pid.write("\n")
        self.__write_type("Group")  
        self.__write_name(equipment.name,"e")  
        self.__write_label(equipment.label,"","")
        self.__write_icon(equipment.icon)
        self.__write_group(equipment.group)
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
        if type(openhabitem) == KnxItem:
            self.__write_bound_to(openhabitem.bound_to)

        #Itemdefintion abgeschlossen. Das nächste Item startet in der nächsten Zeile
        self.pid.write("\n")

    def __write_type(self, type : str):
        self.pid.write(type.strip())
        self.pid.write(self.delimiter)
    
    def __write_name(self, name : str, prefix : str = "i"):
        self.pid.write(name)
        self.pid.write(self.delimiter)

    def __write_label(self, label : str, format : str, einheit : str):
        if label: 
            self.pid.write("\""+ label.strip())
        else:
            raise ValueError("Label nicht gesetzt")

        if format:
            self.pid.write( " [" + format.strip())
            if einheit:
                self.pid.write(self.delimiter)
                self.pid.write( einheit.strip())
            self.pid.write("]")

        if label:
            self.pid.write("\"") 
            self.pid.write(self.delimiter) 

    def __write_icon(self, icon : str):
        if icon and type(icon) == tuple:
            self.pid.write("<ik" + icon[0].strip() + ">")
        elif icon:
            self.pid.write("<ik" + icon[0].strip() + ">")
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


      
