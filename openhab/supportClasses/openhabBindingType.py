
from enum import Enum

class OpenhabBindingType(Enum):
    KNX = 1
    PING_ONLINE = 2
    SERVICE_ONLINE = 3
    PING_LAST_SEEN = 4
    SERVICE_LAST_SEEN =5
    MODBUS = 6
    WETTER = 7
