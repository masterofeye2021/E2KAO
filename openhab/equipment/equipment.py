from openhab.openhab_generic import OpenhabGeneric
import equipment_mapping

class Equipment: 

    name : str
    label : str
    icon : str
    location : str
    group : str

    def __init__(self, data):
        self.icon = data[equipment_mapping.ICON],
        self.location = data[equipment_mapping.LOCALATION]
        self.name = "e" + data[equipment_mapping.NAME]
        self.label = data[equipment_mapping.LABEL]
        self.group = self.set_group(data[equipment_mapping.GROUP1],
            data[equipment_mapping.GROUP2],
            data[equipment_mapping.GROUP3],
            data[equipment_mapping.GROUP4])

        self.name = OpenhabGeneric.__remove_umlaut__(self.name)
        self.icon =  OpenhabGeneric.__remove_umlaut__(self.icon)
        self.location =  OpenhabGeneric.__remove_umlaut__(self.location)
        self.group =  OpenhabGeneric.__remove_umlaut__(self.group)


    def set_group(self,group1:str,group2:str,group3:str,group4:str):
        group = ""

        if group1:
            group += "g" + group1 + ","
        
        if group2:
            group += "g" + group2 + ","
        
        if group3:
            group += "g" + group3 + ","
        
        if group4:
            group += "g" + group4 + ","

        if group.endswith(","):
            group = group.removesuffix(",")

        return group