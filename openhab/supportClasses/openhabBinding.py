
from openhab.supportClasses.openhabBindingType import OpenhabBindingType


class OpenhabBinding:
    def __init__(self, openhabItemType: OpenhabBindingType) -> None:
        self.openhabItemType = openhabItemType
        pass

    def toString(self, item) -> str:
        if self.openhabItemType == OpenhabBindingType.KNX:
            return "{ channel = \"knx:device:bridge:generic:c" + item.name.removeprefix("i") + "\"}"
        elif self.openhabItemType == OpenhabBindingType.PING_ONLINE:
            return "{ channel = \"network:pingdevice:c" +item.name.removeprefix("i") + ":online" + "\"" +"}" 
        elif self.openhabItemType == OpenhabBindingType.SERVICE_ONLINE:
            return "{ channel = \"network:servicedevice:c" +item.name.removeprefix("i") + ":online" + "\"" +"}" 
        elif self.openhabItemType == OpenhabBindingType.PING_LAST_SEEN:
            return "{ channel = \"network:pingdevice:c" +item.name.removeprefix("i").replace("_Last_Seen","") + ":lastseen" + "\"" +"}"
        elif self.openhabItemType == OpenhabBindingType.SERVICE_LAST_SEEN:
            return "{ channel = \"network:servicedevice:c" +item.name.removeprefix("i").replace("_Last_Seen","") + ":lastseen" + "\"" +"}"
        elif self.openhabItemType == OpenhabBindingType.MODBUS:
            return "{ channel = \"modbus:data:pv:c" + item.name.removeprefix("i") + ":" + "c" +  item.name.removeprefix("i") + ":" + item.type.lower()+ "\"}"
        else:
            raise Exception("hier solltest du nicht landen.")