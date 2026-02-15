calcul = input("Put your operation : ")
x, y, z = calcul.split(" ")
x = float(x)
z = float(z)
if y == "+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "/":
    print(x/z)
else:
    print(x*z)