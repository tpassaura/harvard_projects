from cs50 import get_float


# GET USER INPUT
while True:
    try:
        owed = get_float("How much is owed: ")
        if owed > 0:
            break
    except ValueError:
        print("Error")

# ROUND VALUE
change = round(int(owed*100))

# DEFINE NUMBER OF COINS
coins = 0

# CALCULATION OF COINS
while change > 0:
    while change >= 25:
        coins += 1
        change -= 25
    while change >= 10:
        coins += 1
        change -= 10
    while change >= 5:
        coins += 1
        change -= 5
    while change >= 1:
        coins += 1
        change -= 1

# PRINT NUMBER OF COINS
print(coins)

