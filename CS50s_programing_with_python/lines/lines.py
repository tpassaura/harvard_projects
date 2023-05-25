import sys


def main():
    try:
        # Check if size of argv is correct
        if len(sys.argv) != 2:
            raise ValueError
        # Get name of file
        name = sys.argv[1].strip()
        # Check if it is a python file
        if name.split(".")[1] != "py":
            raise ValueError
        else:
            print(count_lines(name))

    except:
        sys.exit(1)


# Count number of lines
def count_lines(name):
    # Open file
    with open(name) as file:
        # Get file lines
        lines = file.readlines()
        num_lines = 0
        # Check each line
        for line in lines:
            line = line.lstrip()
            if line:
                if line.startswith("#") == False:
                    num_lines += 1
        return num_lines


if __name__ == "__main__":
    main()
