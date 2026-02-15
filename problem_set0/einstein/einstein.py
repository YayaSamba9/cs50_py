def calculate():
    mass = int(input("Put an integer number please: "))
    speed_of_light = 300000000
    c = pow(speed_of_light,2)
    energy = mass * c
    print(energy)


calculate()

