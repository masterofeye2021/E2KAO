from time import time
from knx.group_address import GroupAddress
from openhab.items.item import OpenhabItem
from openhab.precessors.iten_name_precessor import ItemNameProcessor
from openhab.precessors.validator_precessor import Validator
import item_mapping
import time

"""
@brief reprensentiert ein Item welches auf dem KNX Binding aufsetzt
@member type Type des Items, abhängig vom zugeordnenten Geräte und der Funktion (z.B.: Switch, String, Number, ...)
@member label 
"""
class KnxItem(OpenhabItem,ItemNameProcessor,Validator):

    #knxaddress : str

    def __init__(self, data):

        self.start = time.time()
        
        location = str(data[item_mapping.LOCALATION]).replace(" ","_") 
        access = str(data[item_mapping.ACCESS]).replace(" ","_") 
        name = str(data[item_mapping.NAME]).replace(" ","_") 
        extention =str(data[item_mapping.EXTENTION]).replace(" ","_") 
        function = str(data[item_mapping.FUNCTION]).replace(" ","_") 

        self.name = self.__create_item_name__(location, access, name, extention, function, "i")

        self.type = data[item_mapping.TYPE]
        self.label = data[item_mapping.LABEL]
        self.format = data[item_mapping.FORMAT]
        self.einheit = data[item_mapping.EINHEIT]
        self.icon = data[item_mapping.ICON]
        self.tag = data[item_mapping.TAG]
        self.boundto = data[item_mapping.BOUND_TO]
        self.equipment = data[item_mapping.EQUIPMENT]
        self.transform = data[item_mapping.TRANSFORM]
        self.group = self.set_group(data[item_mapping.GROUP1],
            data[item_mapping.GROUP2],
            data[item_mapping.GROUP3],
            data[item_mapping.GROUP4])
        self.adresses = []
        self.adresses.append(GroupAddress(data[item_mapping.MAIN],data[item_mapping.MIDDLE],data[item_mapping.SUB]))
        self.adresses.append(GroupAddress(data[item_mapping.MAIN2],data[item_mapping.MIDDLE2],data[item_mapping.SUB2]))
        self.adresses.append(GroupAddress(data[item_mapping.MAIN3],data[item_mapping.MIDDLE3],data[item_mapping.SUB3]))

        if data[item_mapping.PERSISTENCE] == "x": self.persistence= True 
        else:self.persistence=False
        
        ItemNameProcessor.__init__(self)
        Validator.__init__(self)

        self.__check_type__()
        self.__check_name__()
        self.__check_group__()
        self.__check_label__()
        self.__check_icon__()
        self.__check_tag__()
        self.__check_equipment__()
        self.end = time.time()
        print(self.name + ' {:5.3f}s'.format(self.end-self.start))

    
    def set_bound_to(self, channel_uid : str, transform):

        if not transform:
            self.bound_to = "{channel=\""+channel_uid+"\"}"
        elif  ".js" in transform:
            self.bound_to = "{channel=\""+channel_uid+"\"[profile=\"transform:JS\", function=\""+transform+"\"]}"
        else:
            self.bound_to = "{channel=\""+channel_uid+"\"[profile=\"transform:MAP\", function=\""+transform+"\"]}"
    
        if self.type == "DateTime":
            self.bound_to = "{channel=\""+channel_uid +  "\" [profile=\"follow\"],channel=\"ntp:ntp:local:dateTime\""+"}"
