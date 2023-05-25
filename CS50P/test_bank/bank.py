# Request input
def main():
   greeting = input('Greeting: ').lower().strip()
   output = value(greeting)
   print(f'${output}')


def value(greeting):
    first_letter = greeting[0]
    frist_world = greeting.split(' ', 1)[0].split(',')[0]

    if frist_world == 'hello':
        return(0)
    elif first_letter == 'h':
        return(20)
    else:
        return(100)



if __name__ == "__main__":
    main()