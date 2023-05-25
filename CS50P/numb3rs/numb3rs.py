import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    regex_ipv4 = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    # regex_ipv6 = r'^(([0-9a-fA-F]{1,4}):){7}([0-9a-fA-F]{1,4})$'

    if re.match(regex_ipv4, ip):
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()