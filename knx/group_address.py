from dataclasses import dataclass

@dataclass
class GroupAddress:
    main : int = 0
    middle : int = 0
    sub : int = 0