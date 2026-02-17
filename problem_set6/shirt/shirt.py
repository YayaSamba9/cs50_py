from PIL import Image, ImageOps
import sys

def main():
    tests()
    image()

def tests():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    image_types = ["jpg", "jpeg", "png"]
    arg1 = sys.argv[1]
    file1, extension1 = arg1.split(".")

    if extension1 in image_types:
        pass
    else:
        sys.exit("Invalid input")

    arg2 = sys.argv[2]
    file2, extension2 = arg2.split(".")

    if extension2 in image_types:
        pass
    else:
        sys.exit("Invalid output")

    if extension1 != extension2:
        sys.exit("Input and output have different extensions")

def image():
    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as im:
            im = ImageOps.fit(im, shirt.size)
            im.paste(shirt, shirt)
            im.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()

