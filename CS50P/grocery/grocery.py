# Define variables
list = []
results = {}

while True:
    try:
        # Get user input
        item = input().upper().strip()
        # Add item to the list
        list.append(item)

    except EOFError:
        # Sort the list
        list = sorted(list)
        # Count itens and add to the result dic
        for item in list:
            results[item] = results.get(item, 0) + 1
        # Print amount and item 
        for item in results:
            count = results[item]
            print(count ,item)
        break