from cs50 import get_string


def main():
    # ASK USER FOR IMPUT
    text = get_string("Text: ")

    # EXECUTE FUNCTIONS
    textLength = len(text)
    textWords = count_words(text, textLength)
    textSentences = count_senteces(text, textLength)
    textLetters = count_letters(text, textLength)

    # DEFINE L AND S
    L = (textLetters / textWords)*100
    S = (textSentences / textWords)*100

    # PRINT GRADE
    print_grade(L, S)


# FUNCTION TO COUNT LETTERS
def count_letters(text, textLength):
    i = 0
    textLetters = 0
    while i < textLength:
        if text[i].isalpha() == True:
            textLetters += 1
            i += 1
        else:
            i += 1
    return textLetters


# FUNCTION TO COUNT WORDS
def count_words(text, textLength):
    i = 0
    textWords = 1
    while i < textLength:
        if text[i].isspace() == True:
            textWords += 1
            i += 1
        else:
            i += 1
    return textWords


# FUNCTION TO COUNT SENTENCES
def count_senteces(text, textLength):
    i = 0
    textSentences = 0
    while i < textLength:
        if text[i] == "." or text[i] == "?" or text[i] == "!":
            textSentences += 1
            i += 1
        else:
            i += 1
    return textSentences


# FUNCTION TO PRINT GRADE
def print_grade(L, S):
    grade = round(0.0588 * L - 0.29 * S - 15.8)

    if grade < 1:
        print("Before Grade 1")
    if grade > 1 and grade < 16:
        print(f"Grade {grade}")
    if grade > 16:
        print("Grade 16+")


main()