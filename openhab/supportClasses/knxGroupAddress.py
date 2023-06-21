from openhab.supportClasses.knxItemType import KnxItemType


class KnxGroupAddress():
    def __init__(self, main: int, middle: int, sub: int,
                 main2: int, middle2: int, sub2: int,
                 main3: int, middle3: int, sub3: int, type: KnxItemType, dpt: str) -> None:
        self.address1 = str(main) + "/" + str(middle) + "/" + str(sub)
        self.type = type
        if dpt:
            self.dpt = str(dpt) + ":"
        else:
            self.dpt = ""

        if main2 is not None and middle2  is not None and sub2  is not None:
            self.address2 = str(main2) + "/" + str(middle2) + "/" + str(sub2)
        else:
            self.address2 = None
        if main3 is not None and middle3  is not None and sub3  is not None:
            self.address3 = str(main3) + "/" + str(middle3) + "/" + str(sub3)
        else:
            self.address3 = None
        pass

    def toString(self) -> str:
        match self.type:
            case KnxItemType.ROLLERSHUTTER:
                return "[ upDown=\"" + self.address1 + "\" , stopMove=\"" + self.address2 + "\" , position=\"" + self.address3 + "\" ]"
            case KnxItemType.DIMMER:
                return "[ switch=\"" + self.address1 + "\" , position=\"" + self.address2 + "\" , increaseDecrease=\"" + self.address3 + "\" ]"
            case _:
                return "[ ga=\"" + self.dpt + self.address1 + "\" ]"
        

    
