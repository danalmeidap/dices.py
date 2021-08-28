from models.unit import Unit
from models.ten import Ten
from models.hundred import Hundred
from models.eleven_to_nineteen import ElevenToNineteen
from sys import exit


def get_value(msg: str) -> int:
    while True:
        try:
            value: int = int(input(msg))
            if 0 <= value <= 999:
                return value
            else:
                print("The value must be between 0 and 999")
        except (TypeError, ValueError):
            print('The value must be a number')
        except KeyboardInterrupt:
            exit('Interrupted by user')


def number_in_full(number: int) -> str:
    unit: int = number // 1 % 10
    ten: int = number // 10 % 10
    hundred: int = number // 100 % 10
    if len(str(number)) == 3 and ten == 0 and unit == 0:
        return f"{Hundred(hundred)} hundred"
    elif len(str(number)) == 3 and unit == 0:
        return f"{Hundred(hundred)} hundred and {Ten(ten)}"
    elif len(str(number)) == 3 and ten == 0:
        return f"{Hundred(hundred)} hundred and {Unit(unit)}"
    elif len(str(number)) == 3 and ten == 1:
        return f"{Hundred(hundred)} hundred and {ElevenToNineteen(unit)}"
    elif len(str(number)) == 3:
        return f"{Hundred(hundred)} hundred and {Ten(ten)} {Unit(unit)}"
    if len(str(number)) == 2 and ten == 1:
        return f"{ElevenToNineteen(unit)}"
    elif len(str(number)) == 2 and unit == 0:
        return f"{Ten(ten)}"
    elif len(str(number)) == 2:
        return f"{Ten(ten)} {Unit(unit)}"
    return f"{Unit(unit)}"
