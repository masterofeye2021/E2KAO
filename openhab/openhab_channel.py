from dataclasses import dataclass
import json

from knx.group_address import GroupAddress

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
    group_address: GroupAddress = None
    kind : str = "STATE"

    def __post_init__(self):
        self.uid = self.__set_uid__("knx:device", self.uid_hex_value ,self.id)
        self.channel_type = self.__set_item_type__(self.item_type)
        self.configuration = self.__set_configuration(self.group_address.main,
                                                       self.group_address.middle,
                                                       self.group_address.sub)

    def __set_item_type__(self,item_type) -> str:
        if item_type:
            return "knx:" + str.lower(item_type)
        else:
            raise ValueError("item type ungültig")

    def __set_uid__(self, prefix, uid_hex_value , suffix):
        return prefix + ":" + uid_hex_value + ":" +  suffix

    def __set_configuration(self, main:str, middle:str, sub:str):
        return { "ga" :  str(main) + "/" + str(middle) + "/" + str(sub)}

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