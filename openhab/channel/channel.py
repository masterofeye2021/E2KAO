from dataclasses import dataclass

@dataclass
class OpenChannel:
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

    kind : str = "STATE"
    datatype : str = ""

    def __init__(self) -> None:
        pass

    def __set_uid__(self, prefix, uid_hex_value , suffix):
        return prefix + ":" + uid_hex_value 

    def __set_item_type__(self,item_type) -> str:
        if item_type:
            self.channel_type = item_type
        else:
            raise TypeError ("Der Channel hat einen ungültigen Type!")

    def to_json()-> str :
        return ""