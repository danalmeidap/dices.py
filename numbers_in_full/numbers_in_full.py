"""Receives a number between 0 and 999 from user and writes the chosen number in full"""

from operations import get_value, number_in_full


def main() -> None:
    number: int = get_value("Please insert a number between 0 and 999:")
    print(number_in_full(number))


if __name__ == "__main__":
    main()
