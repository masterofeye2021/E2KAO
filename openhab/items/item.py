from dataclasses import dataclass

from openhab.precessors.validator_precessor import Validator


class OpenhabItem():
    type : str
    name : str
    label : str
    format : str
    einheit : str
    group : str
    icon : str
    tag : str
    boundto : str
    equipment : str
    item_prefix : str = "i"
    transform : str = ""
    
    def get_group(self) -> str :
        return self.group

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

    def add_group(self,group:str):
        self.group = self.group + group + ","