from enum import Enum


class Ten(Enum):
    Ten = 1
    Twenty = 2
    Thirty = 3
    Forty = 4
    Fifty = 5
    Sixty = 6
    Seventy = 7
    Eighty = 8
    Ninety = 9

    def __str__(self) -> str:
        return self.name
