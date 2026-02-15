import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    sys.exit(0)

if len(sys.argv) <= 3 or sys.argv[1] != "-f":
    sys.exit("Invalid usage")

font = sys.argv[2]

if font not in figlet.getFonts():
    sys.exit("Invalid font")

text = input("Input: ")

figlet.setFont(font=font)

print("Output: ")
print(figlet.renderText(text))


