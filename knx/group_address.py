from dataclasses import dataclass

@dataclass
class GroupAddress:
    main : int = 0
    middle : int = 0
    sub : int = 0

    def is_valid(self):
        if self.main is None or self.middle is None or self.sub is None:
            raise ValueError("Gruppen Adresse ist nicht gültig!")