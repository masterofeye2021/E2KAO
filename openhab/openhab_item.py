from dataclasses import dataclass

@dataclass 
class ItemName:
    place : str
    access : str
    name : str
    extention : str
    function : str 
    item_prefix : str 

    def __post_init__(self):
        self.name = self.name.strip()
        self.name = self.name.replace(" ","_")

        self.place = self.place.strip()
        self.place = self.place.replace(" ","_")

        if self.function:
            self.function.strip()
            self.function = self.function.replace(" ","_")

        if self.extention:
            self.extention.strip()
            self.extention = self.extention.replace(" ","_")

    def get_name(self, prefix:str) -> str :

        var = ""
        delimiter = "_"

        var += prefix

        if self.place:
            var += self.place + delimiter

        #nur wenn auch der erste Prefix gesetzt ist, wird auch der zweite genutzt
        if self.access:
            var += self.access + delimiter

        if self.name:
            var += self.name

        if self.extention:
            var += delimiter
            var += self.extention

        #nur wenn auch der erste Suffix gesetzt ist, wird auch der zweite genutzt
        if self.function:
            var += delimiter
            var += self.function

        return var


@dataclass
class OpenhabItem:
    type : str
    name : ItemName
    label : str
    format : str
    einheit : str
    group : str
    icon : str
    tag : str
    bound_to : str
    equipment : str
    item_prefix : str = "i"

    def __post_init__(self):
        if not self.type:
            raise ValueError("Datenfeld für den Itemtype darf nicht leer sein!")
        if not self.name:
            raise ValueError("Datenfeld für den Name darf nicht leer sein!")
        if not self.label:
            raise ValueError("Datenfeld für das Label darf nicht leer sein!")
        if not self.group:
            raise ValueError("Datenfeld für die Gruppe darf nicht leer sein!")
        if not self.icon:
            raise ValueError("Datenfeld für das Icon darf nicht leer sein!")
        if not self.tag:
            raise ValueError("Datenfeld für deb Tag darf nicht leer sein!")


    def __set_bound_to__(self, channel_uid):
        self.bound_to = "{channel=\""+channel_uid+"\"}"


