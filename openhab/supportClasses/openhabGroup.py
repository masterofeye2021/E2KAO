class OpenhabGroup:
    def __init__(self) -> None:
        self.groups = []

    def addGroup(self, group: str) -> None:
        if group or (group != None):
            self.groups.append(group)

    """
    @brief Gibt die Gruppenzuorndnung eines Items als kommaseparierte Liste zurück.
    """

    def getGroup(self) -> str:
        return ", ".join(self.groups)

    def toString(self) -> str:
        return "(" + self.getGroup().replace(" ", "_") + ")"
