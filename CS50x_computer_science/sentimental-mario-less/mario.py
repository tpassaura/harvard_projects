from cs50 import get_int


# get height
while True:
    try:
        height = get_int("Height: ")
        if (height > 0) and (height <= 8):
            break
    except:
        print("", end="")

spaces = 1
# print newline
for i in range(height):

    # print spaces
    for spaces in range(height-i-1):
        print(" ", end="")

    # prints "#"
    for j in range(i+1):
        print("#", end="")

    print()