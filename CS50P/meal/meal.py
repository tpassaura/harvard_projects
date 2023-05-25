def main():
    # Get time from user
    time = input('What time is it? ')
    # Use function convert to convert input in decimal time
    time = convert(time)

    # Check time and determine meal
    if 7 <= time <= 8:
        print('breakfast time')

    elif 12 <= time <= 13:
        print('lunch time')

    elif 18 <= time <= 19:
        print('dinner time')
    else:
        exit

# Function to convert time in decimal time
def convert(time):
    hours =  float(time.split(':', 2)[0])
    minutes = float(time.split(':', 2)[1])/60

    return hours + minutes



if __name__ == "__main__":
    main()