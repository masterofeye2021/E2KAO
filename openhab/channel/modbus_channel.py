import json
from lib2to3.pytree import type_repr
from plistlib import UID
import api_caller
import item_mapping
from knx.group_address import GroupAddress
from openhab.channel.channel import OpenChannel
from openhab.openhab_generic import OpenhabGeneric
from openhab.thing_map import ThingMap


class ModbusChannel(OpenChannel):

    def __init__(self,data) -> None:
        self.uuidKNX = data[item_mapping.UUID]
        self.uuidChannel = data[item_mapping.UUID] 
        self.__check__uuid()
        
    def __check__uuid(self):
        if not self.uuidKNX :
            raise TypeError("UUID ist nicht gesetzt.")

