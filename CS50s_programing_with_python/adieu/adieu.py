import inflect
p = inflect.engine()

def main():
    # Crate list for names
    names = []
    while True:
        try:
            # Get user input
            name = input('Name: ').strip()
            # Add input to list
            names.append(name)

        # End loop when control + D is pressed
        except EOFError:
            print()
            break

    # Define and print output
    output = p.join(names)
    print('Adieu, adieu, to '+ output)

main()
