from tabulate import tabulate
import sys
import csv

def main():
    try:
        # Check if size of argv is correct
        if len(sys.argv) != 2:
            raise ValueError
           # Get name of file
        name = sys.argv[1].strip()
        # Check if it is a python file
        if name.split(".")[1] != "csv":
            raise ValueError
        else:
            # Print table
            print_table(name)

    except Exception as e:
        sys.exit(1)

# Fucntion to print table
def print_table(name):
    # Open file
    with open(name) as file:
        # Read csv
        reader = csv.DictReader(file)
        # Print table with
        print(tabulate(reader,headers="keys" , tablefmt="grid"))

if __name__ == "__main__":
    main()