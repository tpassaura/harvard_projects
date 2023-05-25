import random


def main():
    # Define game level
    level = get_level()

    # Iniciate score
    score = 0
    # Creat 10 questions
    for _ in range(10):
        x, y = generate_integer(level)
        result = x + y
        # Check if awnser is correct
        count_tries = +1
        while count_tries <= 3:
            try:
                answer = int(input(f'{x} + {y} = '))
                if answer != result:
                    if count_tries == 3:
                        print(f'{x} + {y} = {result}')
                        break
                    else:
                        count_tries += 1
                        print('EEE')
                        raise ValueError
                else:
                    score += 1
                    break

            except ValueError:
                pass

    print(f'Score: {score}')

# Define game level
def get_level():
    #ask for level between 1 and 3
    while True:
        try:
            level = int(input('Level: '))
            if level in [1,2,3]:
                return level
            else:
                raise ValueError
        except ValueError:
            pass

# Generate random integers based on level
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    if level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level ==3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

if __name__ == "__main__":
    main()