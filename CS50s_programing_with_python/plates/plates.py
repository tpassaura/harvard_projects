def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if valid_size(s) == True:
        if valid_chars(s) == True:
            if valid_start(s) == True:
                if valid_sequence(s) == True:
                    return True


def valid_size(s):
    if 2 <= len(s) <= 6:
        return True
# Check if all characters are valid
def valid_chars(s):
    if s.isalnum() == True:
        return True
 # Check if the frist two letters is alpha
def valid_start(s):
    if s[0:2].isalpha() == True:
        return True

 # check if sequence of characters is correct
def valid_sequence(s):
    num_found = False
    for i in range(len(s)):
        letter = s[i]
        # Check if the digit is a frist number and is 0
        if s[i].isdigit() and num_found == False and s[i] == '0':
            return False
        # Check if the digit is a frist number and is not 0
        elif s[i].isdigit() and num_found == False and s[i] != '0':
            num_found = True
        # Check if there is a letter after a number
        elif num_found == True and s[i].isalpha():
            return False

    return True

main()