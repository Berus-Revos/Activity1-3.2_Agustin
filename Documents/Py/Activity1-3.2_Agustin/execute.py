from main30 import Balance

account = Balance(name="Tin", starting_money=0)
while True:
    print(f"{"Profile":^10}\nName: {account.name}\nMoney: {account.money}\nBank Balance: {account.balance}\nStuff_Done: {account.stuff_done}")

    print("1. Bank Management\n2. Work\n3. Buy/Shop\n4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Inavlid Input!")

    match choice:
        case 1: account.bank()
        case 2: account.work()
        case 3: account.shopping()
        case 4: break
        case _: print("Invalid Input")