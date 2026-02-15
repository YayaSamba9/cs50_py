name = input("What's your name? ")

file = open("test2.txt", "a")
file.write(f"{name}\n")
file.close()