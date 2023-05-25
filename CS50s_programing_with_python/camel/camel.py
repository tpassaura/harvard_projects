# Get user input
variable = input('camelCase: ')

# Print start of answer
print('snake_case: ', end='')

# Print each letter converted
for index in range(len(variable)):
    if variable[index].islower():
        print (variable[index], end='')

    else:
        print(f'_{variable[index].lower()}', end='')

# Print new line
print()