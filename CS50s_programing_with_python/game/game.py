import random

# Ask user a valid level
while True:
    try:
        level = int(input("Level: "))
        # Get a random number
        result = random.randrange(1, level + 1)
        # Check if level is grater than 0
        if level < 1:
            pass
        else:
            break

    except:
        pass

# Ask user to valid Guess
while True:
    try:
        guess = int(input("Guess: "))
        # Check if guess is grater than zero
        if level < 1:
            pass
        else:
            # Check if the guees is smaller
            if guess < result:
                print("Too small!")
                pass
            # Check if the guees is grater
            elif guess > result:
                print("Too large!")
                pass
            # If Guess is right
            else:
                print("Just right!")
                break

    except:
        pass
