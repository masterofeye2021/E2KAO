from openhab.items.item import OpenhabItem
from openhab.precessors.iten_name_precessor import ItemNameProcessor
from openhab.precessors.validator_precessor import Validator
import item_mapping

"""

"""
class EkeyItem(OpenhabItem,ItemNameProcessor,Validator):
    def __init__(self, data):
        location = data[item_mapping.LOCALATION]
        access = data[item_mapping.ACCESS]
        name = data[item_mapping.NAME]
        extention =data[item_mapping.EXTENTION]
        function = data[item_mapping.FUNCTION]     

        self.name = self.__create_item_name__(location, access, name, extention, function)

        self.type = data[item_mapping.TYPE]
        self.label = data[item_mapping.LABEL]
        self.format = data[item_mapping.FORMAT]
        self.einheit = data[item_mapping.EINHEIT]
        self.icon = data[item_mapping.ICON]
        self.tag = data[item_mapping.TAG]
        self.boundto = data[item_mapping.BOUND_TO]
        self.equipment = data[item_mapping.EQUIPMENT]


        return super().__init__()

        
    def __post_init__(self):
        self.__check_type__()
        self.__check_name__()
        self.__check_group__()
        self.__check_label__()
        self.__check_icon__()
        self.__check_tag__()
        self.__check_equipment__()
        return super().__post_init__()
    