import sys
import re
from datetime import date
import inflect

p = inflect.engine()


class Born:
    def __init__(self, date, dif):
        self.date = date

    def __str__(self):
        return f"{self.date}"

    @classmethod
    def get(cls):
        birth = input("Birth date: ")
        check = birth
        if check := re.search(r"^([0-9]{4})\-([0-9]{2})\-([0-9]{2})$", check):
            year = int(check.group(1))
            month = int(check.group(2))
            day = int(check.group(3))
            if month <= 12 and day <= 31:
                birth = date(year, month, day)
                return birth
            else:
                sys.exit("Invalid date format")
        else:
            sys.exit("Invalid date format")


class Today:
    @classmethod
    def get(cls):
        return date.today()


def convert(minutes):
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"


def main():
    born = Born.get()
    today = Today.get()
    dif = today - born
    minutes = dif.days * 1440
    print(convert(minutes))


if __name__ == "__main__":
    main()
