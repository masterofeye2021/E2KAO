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

        if place and not place == 'None':
            var += place + delimiter

        #nur wenn auch der erste Prefix gesetzt ist, wird auch der zweite genutzt
        if access and not access== 'None':
            var += access + delimiter

        if name and not name == 'None':
            var += name

        if extention and not extention == 'None':
            var += delimiter
            var += extention

        #nur wenn auch der erste Suffix gesetzt ist, wird auch der zweite genutzt
        if function and not function == 'None':
            var += delimiter
            var += function

        return OpenhabGeneric.__remove_umlaut__(var)