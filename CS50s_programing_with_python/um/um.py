import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    expression = r"(?i)\bum\b"

    matches = re.findall(expression, s)
    return (len( matches))


if __name__ == "__main__":
    main()