
class ThingMap() :

    def __init__(self):
        self._thing_map : dict = dict()
        pass

    def add_thing(self, thing_id: str, thing: any, ) :
        self._thing_map[thing_id] = thing

    def get_thing(self, thing_id:str) :
        for i in self._thing_map.keys():
            if thing_id in i:
                return self._thing_map[i]
        return None

    def contains_thing(self, thing_id:str) -> bool :
        if thing_id in self._thing_map:
            return True
        else:
            return False

