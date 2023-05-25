import sys
import requests


# Get user input
def main():
    try:
        # Check if arvg exist and convert to float
        n = float(sys.argv[1])
        # Make a request from bitcoin API
        request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    except:
        sys.exit(1)

    else:
        # Trasnforme request responde in json
        response = request.json()
        # Extract UDS bitcoin value from json
        rate = float(response["bpi"]["USD"]["rate_float"])
        # Calculate value and print
        exchanged = n * rate
        print(f"${exchanged:,.4f}")


main()
