
def main():
    text = input('Input: ')
    output = shorten(text)
    print (output)


def shorten(word):
    output = ''
    for letter in range(len(word)):
        match word[letter]:
            case 'A'|'a'|'E'|'e'|'I'|'i'|'O'|'o'|'U'|'u':
                new_letter = ''
                output += new_letter
            case _ :
                new_letter = word[letter]
                output += new_letter
    return output


if __name__ == "__main__":
    main()