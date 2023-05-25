def main():
    # Def variables
    due = 50
    total = 0

    # While due is gratter than zero keep ketting coin
    while due > 0:
        coin = get_coin(due)
        due = due - coin
        total = total + coin
        print(f'Amount Due: {due}')

    owed = total - 50
    print(f'Change Owed: {owed}')



def get_coin(due):
    coin = None
    while coin != 25 and coin != 10 and coin != 5:
        coin = int(input('Insert Coin: '))
        print(f'Amount Due: {due}')
    return (coin)

main()
