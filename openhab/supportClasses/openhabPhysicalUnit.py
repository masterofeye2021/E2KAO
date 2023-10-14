from strenum import StrEnum


class OpenhabPhysicalUnit(StrEnum):
    NONE ="",
    KM = "km",
    KMH = "km/h",
    C = "°C",
    PPM = "ppm",
    LUX = "lux",
    W = "W",
    KW = "kW"
    WH = "Wh"
    KWH = "kWh"
    H = "h"
    PROZENT = "%"
    UNIT = "%unit%"

    @classmethod
    def _missing_(cls, value):
        return cls.NONE
