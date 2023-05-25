from cs50 import get_int

def main():
    while True:
        n = get_int("Height: ")
        if (n < 1 and n > 8):
            break
        print_dash(n)

def print_dash(n):
    while True:
        print("#")
        n = n -1

        if (n == 0):
            break

main()