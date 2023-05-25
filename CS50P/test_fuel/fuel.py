def main():
            # Get user input
            fraction = input('Fraction: ')
            porcentage = convert(fraction)
            print(gauge(porcentage))

def convert(fraction):
    # Define X and Y
    x = int(fraction.split('/')[0])
    y = int(fraction.split('/')[1])

    # Check if value is correct
    try:
        return int((x/y) * 100)
    except (ValueError,ZeroDivisionError):
        raise


def gauge(percentage):
    # Print porcentage
    if percentage <= 1:
        return('E')
    elif percentage >= 99:
        return('F')
    else:
        return(f'{percentage}%')


if __name__ == "__main__":
    main()