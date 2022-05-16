from dataclasses import dataclass
import json

from knx.group_address import GroupAddress

ROLLERSHUTTER  = "Rollershutter"
DIMMER  = "Dimmer"


@dataclass
class OpenhabChannel:
    uid : str = ""
    uid_hex_value : str = ""
    id : str = ""
    item_type : str = ""
    channel_type : str = ""
    label : str = ""
    description : str = ""
    default_tags : list[str] = None
    property : dict = None 
    configuration : dict = None
    group_address: list[GroupAddress] = None
    kind : str = "STATE"

    def __post_init__(self):
        self.uid = self.__set_uid__("knx:device", self.uid_hex_value ,self.id)
        self.channel_type = self.__set_item_type__(self.item_type)
        self.configuration = self.__set_configuration(self.group_address)

    def __set_item_type__(self,item_type) -> str:
        if item_type:
            return "knx:" + str.lower(item_type)
        else:
            raise ValueError("item type ungültig")

    def __set_uid__(self, prefix, uid_hex_value , suffix):
        return prefix + ":" + uid_hex_value + ":" +  suffix

    def __set_configuration(self, group_address : list[GroupAddress]):
        for g in group_address:
            g.is_valid()

        if self.item_type == ROLLERSHUTTER :

            return  { "switch" :  str(group_address[0].main) + "/" + str(group_address[0].middle) + "/" + str(group_address[0].sub),
                    "position" :  str(group_address[1].main) + "/" + str(group_address[1].middle) + "/" + str(group_address[1].sub),
                    "increaseDecrease" :  str(group_address[2].main) + "/" + str(group_address[2].middle) + "/" + str(group_address[2].sub),
                    } 
        elif self.item_type == DIMMER:
            return  { "upDown" :  str(group_address[0].main) + "/" + str(group_address[0].middle) + "/" + str(group_address[0].sub),
                    "stopMove" :  str(group_address[1].main) + "/" + str(group_address[1].middle) + "/" + str(group_address[1].sub),
                    "position" :  str(group_address[2].main) + "/" + str(group_address[2].middle) + "/" + str(group_address[2].sub),
                    } 
        else:
            return { "ga" :  str(group_address[0].main) + "/" + str(group_address[0].middle) + "/" + str(group_address[0].sub)}
    
    def json(self):
        return str(
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
        )