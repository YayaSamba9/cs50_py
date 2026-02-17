import csv
import sys
from tabulate import tabulate

def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # Validate file extension
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Read and display CSV file
    read_csv(filename)


def read_csv(filename):
    """Reads a CSV file and displays its contents in a formatted table."""
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            print(tabulate(reader, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


# Program entry point
if __name__ == "__main__":
    main()
