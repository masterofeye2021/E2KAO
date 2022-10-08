import json
from lib2to3.pytree import type_repr
from plistlib import UID
import api_caller
import item_mapping
from knx.group_address import GroupAddress
from openhab.channel.channel import OpenChannel
from openhab.openhab_generic import OpenhabGeneric
from openhab.thing_map import ThingMap

ROLLERSHUTTER  = "Rollershutter"
DIMMER  = "Dimmer"


class KnxChannel(OpenChannel):

    def __init__(self,data,item, thing_map : ThingMap) -> None:

        self.item_type = data[item_mapping.TYPE]
        self.label = data[item_mapping.LABEL]
        self.group_address = item.adresses
        self.data_type= data[item_mapping.BINDING]  
        self.name = "c" + str(item.name).removeprefix("i")  
        self.uuidKNX = data[item_mapping.UUID]
        self.uuidChannel = data[item_mapping.UUID] 
        self.__check__uuid()

        self.uuidChannel = self.uuidChannel + ":" + item.name

        self.channel_type = self.__set_channel_type__(self.item_type)
        self.configuration = self.__set_configuration__(item.adresses)

        if not thing_map.contains_thing(self.uuidKNX):
            thing = api_caller.get_thing_by_uid(self.uuidKNX)
        else:
            thing = thing_map.get_thing(self.uuidKNX)
        thing["channels"].append(self.to_json())
        if not thing_map.contains_thing(self.uuidKNX):
            thing_map.add_thing(self.uuidKNX,thing)
        

    def __set_channel_type__(self,item_type) -> str:
        if item_type:
            return "knx:" + str.lower(item_type)
        else:
            raise TypeError ("Der Channel hat einen ungültigen Type!")

    def __check__uuid(self):
        if not self.uuidKNX :
            raise TypeError("UUID ist nicht gesetzt.")

    def __set_configuration__(self, group_address):
        for g in group_address:
            g.is_valid()

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

    def __check_uuid_exists__(self) :
        return api_caller.get_thing_by_uid(self.uuid)

    def to_json(self)-> any :
        return json.loads(str(
            "{\"linkedItems\": [],"+
            " \"uid\": \"" + self.uuidKNX+":" + self.name + "\"," +
            " \"id\": \""  +  self.name + "\"," +
            " \"channelTypeUID\": \"" + self.channel_type + "\"," +
            " \"itemType\": \"" + self.item_type + "\","+
            " \"kind\": \"" + self.kind + "\","+
            " \"label\": \"" + self.label + "\","+
            " \"description\": \"" + "" + "\","+
            " \"defaultTags\": " + "[]" + ","+
            " \"properties\": " + "{}" + ","+
            " \"configuration\": " + json.dumps(self.configuration) + "}"
        ))