import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    rgx_t_mth = r'(?<!\w)um(?!\w)'
    matches = re.findall(rgx_t_mth, s, re.IGNORECASE)
    return len(matches)


...


if __name__ == "__main__":
    main()
