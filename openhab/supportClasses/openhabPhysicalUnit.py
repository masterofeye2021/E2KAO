from strenum import StrEnum


class OpenhabPhysicalUnit(StrEnum):
    NONE ="",
    KM = "km",
    KMH = "km/h",
    C = "°C",
    PPM = "ppm",
    LUX = "lux",
    W = "w",
    KW = "kW"

    @classmethod
    def _missing_(cls, value):
        return cls.NONE
