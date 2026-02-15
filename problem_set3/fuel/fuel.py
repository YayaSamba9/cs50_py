def main():
    pourcetage = fuel_code()
    if pourcetage <= 1:
        print("E")
    elif pourcetage >= 99 :
        print("F")
    else:
         print(f" tank is {pourcetage} % full ")  
    return pourcetage

def fuel_code():
    while True:
        try:
            frac = input("Fraction: ")
            x,y = frac.split("/")
            x_int = int(x)
            y_int = int(y)
            if x_int>y_int or y_int <= 0 or x_int <0:
                    raise ValueError
            result = round((x_int/y_int)*100)  
            return result
        except (ValueError, ZeroDivisionError):
                pass


main()