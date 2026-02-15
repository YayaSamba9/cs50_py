import sys
def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            back = gauge(percentage)
            print(back)
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x,y = fraction.split("/")
    x_int = int(x)
    y_int = int(y)
    if y_int == 0:
        raise ZeroDivisionError
    if x_int < 0 or x_int > y_int :
        raise ValueError
    return round((x_int/y_int)*100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
