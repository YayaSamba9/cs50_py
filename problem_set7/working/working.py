import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match= re.search(r"^([0-9]{1,2})(?::([0-5][0-9]))? (AM|PM) to ([0-9]{1,2})(?::([0-5][0-9]))? (AM|PM)$",
        s)
    if not match:
        raise ValueError("Invalid Format" )

    hr_1, minu_1, pr_1, hr_2, minu_2, pr_2 = match.groups()
    hr_1, hr_2 = int(hr_1), int(hr_2)
    minu_1 = int(minu_1) if minu_1 else 0
    minu_2 = int(minu_2) if minu_2 else 0

    if not (1<=hr_1 <=12 and 1 <= hr_2 <=12):
        raise ValueError("Invalid Hours range" )
    if not (0 <= minu_1 <60 and 0<=minu_2 < 60):
        raise ValueError("Invalid Minute range ")

    if pr_1 == 'AM' and hr_1 ==12:
        hr_1 = 0
    elif pr_1== 'PM' and hr_1 != 12:
        hr_1 +=12


    if pr_2 == 'AM' and hr_2== 12:
        hr_2 = 0
    elif pr_2 == 'PM' and hr_2 != 12:
        hr_2 += 12

    return f"{hr_1:02}:{minu_1:02} to {hr_2:02}:{minu_2:02}"


if __name__ == "__main__":
    main()
