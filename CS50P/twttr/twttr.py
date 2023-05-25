# Get user input
text = input('Input: ')

for letter in range(len(text)):
    match text[letter]:
        case 'A'|'a'|'E'|'e'|'I'|'i'|'O'|'o'|'U'|'u':
            new_letter = ''
        case _ :
            new_letter = text[letter]
    print(new_letter, end='')

print('')