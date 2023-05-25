# Request input
greeting = input('Greeting: ').lower().strip()

first_letter = greeting[0]
frist_world = greeting.split(' ', 1)[0].split(',')[0]

if frist_world == 'hello':
    print('$0')
elif first_letter == 'h':
    print('$20')
else:
    print('$100')