from openhab.openhab_generic import OpenhabGeneric
from openhab.precessors.precessor import Precessor


class Validator (Precessor):
    
    """
    @brief prüft das Feld type ob ein gültiger Wert gesetzt ist
    """
    def __init__(self) -> None:
        super().__init__()

    def __check_type__(self):
        if not self.type:
            raise TypeError("Datenfeld für den Itemtype darf nicht leer sein!")
        else:
            #Für Items spielen Control Elemente keine Rolle, d.h. wird können einfach openhab typen verwenden
            if self.type == "switch-control":
                self.type = "Switch"
            if self.type  == "datetime-control": 
                self.type = "DateTime"
            if self.type == "contact-control": #TODO check
                self.type = "Control"
            if self.type == "number-control": #TODO check
                self.type = "Number"
            if self.type == "string-control": #TODO check
                self.type = "String"
            if self.type == "dimmer-control": #TODO check
                self.type = "Dimmer"

    def __check_name__(self):
        if not self.name:
            raise TypeError("Datenfeld für den Namen darf nicht leer sein!")
        if len(str.split(self.name,"_")) <= 2:
            raise TypeError("Ungültige Syntax für den Namen entdeckt!")
        if "#" in self.name:
            self.name = self.name.replace("#", "_") 
    
    def __check_label__(self):
        if not self.label:
            raise TypeError("Datenfeld für das Label darf nicht leer sein!")
        if type(self.label) != str:
            raise TypeError("Label sollte vom Typ String sein!")
    def __check_group__(self):
        if not self.group:
            raise TypeError("Datenfeld für die Gruppe darf nicht leer sein!")
        else:
             self.group = OpenhabGeneric.__remove_umlaut__(self.group)
             self.group = self.group.replace(" ","_")
        
    def __check_icon__(self):
        if not self.icon:
            raise TypeError("Datenfeld für das Icon darf nicht leer sein!")
        else:
             self.icon = OpenhabGeneric.__remove_umlaut__(self.icon)
             self.icon = self.icon.replace(" ","_")

    def __check_tag__(self):
        if not self.tag:
            raise ValueError("Datenfeld für deb Tag darf nicht leer sein!")
        else:
            self.tag = OpenhabGeneric.__remove_umlaut__(self.tag)

    def __check_equipment__(self):
        if self.equipment:
            self.equipment = OpenhabGeneric.__remove_umlaut__(self.equipment)