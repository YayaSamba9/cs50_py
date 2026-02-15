def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) <2 or len(s)>6 :
        return False
    if s.isalnum()== False:
        return False
    if s[:2].isalpha()== False:
        return False
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i+1].isalpha():
            return False
    for i in s: 
        if i.isdigit():
            return i != '0'
        else:
            return True
    if s.isnumeric():
        if s[0]==0:
            return False

    

main()