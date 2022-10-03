from platform import processor
from openhab.openhab_generic import OpenhabGeneric

from openhab.precessors.precessor import Precessor
"""
# @brief Diese Klasse erzeugt bassierend auf den Eingabewerten den Itemnamen
"""
class ItemNameProcessor(Precessor) :
    def __init__(self) -> None:

        super().__init__()

    
    def __create_item_name__(self, place:str, access:str, name:str, extention:str, function:str, item_prefix:str) -> str :
        var = ""
        delimiter = "_"

        var += item_prefix

        if place:
            var += place + delimiter

        #nur wenn auch der erste Prefix gesetzt ist, wird auch der zweite genutzt
        if access:
            var += access + delimiter

        if name:
            var += name

        if extention:
            var += delimiter
            var += extention

        #nur wenn auch der erste Suffix gesetzt ist, wird auch der zweite genutzt
        if function:
            var += delimiter
            var += function

        var = var.replace("#","_")
        return OpenhabGeneric.__remove_umlaut__(var)