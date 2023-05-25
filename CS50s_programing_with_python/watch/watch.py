import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    expression = r'<iframe[^>]*src="([^"]+)"[^>]*>'
    match = re.search(expression, s)

    try:
            url = match.group(1)
            id = re.search(r'/embed/([^\?]+)', url).group(1)
            return f"https://youtu.be/{id}"
    except:
         return None




if __name__ == "__main__":
    main()