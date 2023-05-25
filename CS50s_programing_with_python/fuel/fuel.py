while True:
    try:
        # Get user input
        fraction = input('Fraction: ')
        # Define X and Y
        x = int(fraction.split('/')[0])
        y = int(fraction.split('/')[1])

        # Check if value is correct
        if x > y:
            raise ValueError
        else:
            # Calculate porcentage
            porcent = round((x / y) * 100)
            # Print porcentage
            if porcent <= 1:
                print('E')
            elif porcent >= 99:
                print('F')
            else:
                print(f'{porcent}%')

    # Handle errors
    except (ValueError, ZeroDivisionError):
        pass

    else:
        break