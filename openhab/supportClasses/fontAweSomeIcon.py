
class FontAweSomeIcon():
    def __init__(self, icon :str) -> None:
        self._icon = icon
        pass

    def toString(self) -> str:
        if " " in  self._icon:
            raise Exception("Leerzeichen in Icon gefunden.")

        return "<" + self._icon + ">"
