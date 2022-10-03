import json
from plistlib import UID
import api_caller
import item_mapping
from knx.group_address import GroupAddress
from openhab.channel.channel import OpenChannel

ROLLERSHUTTER  = "Rollershutter"
DIMMER  = "Dimmer"


class KnxChannel(OpenChannel):
    group_address: list[GroupAddress] = None
    data_type : str

    def __init__(self,data,group_address) -> None:

        self.channel_type = data[item_mapping.TYPE],
        self.item_type = data[item_mapping.TYPE],
        self.label = data[item_mapping.LABEL],
        self.group_address: [] = group_address,
        self.data_type= data[item_mapping.DATENTYP]      

        self.id = api_caller.get_knx_device_uid()
        self.uid_hex_value = api_caller.get_uid_hex_value(self.id)
        self.uid = self.__set_uid__("knx:device", self.uid_hex_value ,"")
        self.channel_type = self.__set_item_type__(self.item_type)
        self.configuration = self.__set_configuration(group_address)
        self.get_thing()["channels"].append(self.to_json())

    def set_item_type(self,item_type) -> str:
        if item_type:
            return "knx:" + str.lower(item_type)
        else:
            raise TypeError ("Der Channel hat einen ungültigen Type!")

    def __set_configuration(self, l):
        for group_address in l:
            group_address.is_valid()

        if self.item_type == DIMMER :

            return  { "switch" :  str(group_address[0].main) + "/" + str(group_address[0].middle) + "/" + str(group_address[0].sub),
                    "position" :  str(group_address[1].main) + "/" + str(group_address[1].middle) + "/" + str(group_address[1].sub),
                    "increaseDecrease" :  str(group_address[2].main) + "/" + str(group_address[2].middle) + "/" + str(group_address[2].sub),
                    } 
        elif self.item_type == ROLLERSHUTTER:
            return  { "upDown" :  str(group_address[0].main) + "/" + str(group_address[0].middle) + "/" + str(group_address[0].sub),
                    "stopMove" :  str(group_address[1].main) + "/" + str(group_address[1].middle) + "/" + str(group_address[1].sub),
                    "position" :  str(group_address[2].main) + "/" + str(group_address[2].middle) + "/" + str(group_address[2].sub),
                    } 
        else:
            if self.datatype :
                return { "ga" :  str(self.datatype) + ":" + str(group_address[0].main) + "/" + str(group_address[0].middle) + "/" + str(group_address[0].sub)}
            else:
                return { "ga" :  str(group_address[0].main) + "/" + str(group_address[0].middle) + "/" + str(group_address[0].sub)}

    def get_thing(self) :
        return api_caller.get_thing_by_uid(self.uid)


    def to_json(self)-> any :
        return json.loads(str(
            "{\"linkedItems\": [],"+
            " \"uid\": \"" + self.uid + "\"," +
            " \"id\": \""  +  self.id + "\"," +
            " \"channelTypeUID\": \"" + self.channel_type + "\"," +
            " \"itemType\": \"" + self.item_type + "\","+
            " \"kind\": \"" + self.kind + "\","+
            " \"label\": \"" + self.label + "\","+
            " \"description\": \"" + self.description + "\","+
            " \"defaultTags\": " + "[]" + ","+
            " \"properties\": " + "{}" + ","+
            " \"configuration\": " + json.dumps(self.configuration) + "}"
        ))