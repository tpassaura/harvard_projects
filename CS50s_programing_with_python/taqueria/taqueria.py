def main():

    # Define menu itens
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

    # Define order
    order = []
    while True:

        try:
            #Get user input
            item = input('Item: ').title()
            # Search price in menu
            price = menu.get(item)
            # Check item is in meni
            if price != None:
                # Add new tem price to the order
                order.append(price)
                total = 0
                # Calculate the total and print
                for price in order:
                    total = price + total
                print(f"Total: ${total:.2f}")
            # If item not in menu
            else:
                pass

        except EOFError:
            print('')
            break


main()