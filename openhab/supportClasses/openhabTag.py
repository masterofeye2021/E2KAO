class OpenhabTag:
    def __init__(self, tag: str) -> None:
        self.tag = tag
        pass

    def toString(self) -> str:
        return "[\"" + self.tag +  "\"]"