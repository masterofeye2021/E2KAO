from openhab.things.thing import Thing

class ModbusThing(Thing):
    def __init__(self,name: str,  label: str, address : str, type: str, id : int ) -> None:
        self.label = label
        self.adress = address
        self.type = type
        self.poller  = id 
        super().__init__(name)