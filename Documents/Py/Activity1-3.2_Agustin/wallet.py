# TIN's WALLET SIMULATION
# activity 1
# activity 2
# activity 3.2
import random
from PIL import Image, ImageDraw, ImageFont

class Balance:
    def __init__(self, name, starting_money=0):
        self.name = name
        self.starting_money = starting_money
        self.money = starting_money
        self.balance = 0
        self.stuff_done = 0

    def showbalance(self, file="output.png"):
        self.total = self.money + self.balance
        status = {
            "Name": self.name,
            "Money": f"${self.money:,.2f}",
            "Bank Balance": f"${self.balance:,.2f}",
            "Stuff Done": self.stuff_done,
            "Total Money": f"${self.total:,.2f}",
        }
        text = "\n".join(f"{k}: {v}" for k, v in status.items())

        img = Image.new("RGB", (1080, 720), color="white")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 40)
        draw.text((20, 20), text, fill="black", font=font)
        img.save(file)
        img.show()

    def withdraw(self):
        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Invalid Input")
            return
        
        if amount is None or amount <= 0:
            print("Inavlid Input!")
            return
        elif amount > self.balance:
            print("Insufficient Balance!")
            return
        
        self.money += amount
        self.balance -= amount
        self.stuff_done += 1
        print("Withdrawal Success!")
            
    def deposit(self):
        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Invalid Input")

        if amount is None or amount <= 0:
            print("Inavlid Input!")
            return
        elif amount > self.money:
            print("Insufficient Money!")
            return

        self.money -= amount
        self.balance += amount
        self.stuff_done += 1
        print("Deposit Success!")

    def bank(self):
        print("Bank Management\n1. Show Balance\n2. Withdraw\n3. Deposit\n4. Back")
        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid Input")
        match choice:
            case 1: self.showbalance()
            case 2: self.withdraw()
            case 3: self.deposit()
            case 4: return
            case _: print("Invalid Input!")

    def work(self):
        print("Job Site\n1. Construction (100$/day\n2. Cafe (50$/day\n3. Babysitting (20$/day\n4. Back")
        try:
            choice = int(input("Enter the choice: "))
        except:
            print("Invalid Input")
            return
        match choice:
            case 1: gain, work = 100, "Construction"
            case 2: gain, work = 50, "Cafe"
            case 3: gain, work = 20, "Babysitting"
            case 4: return
            case _: print("Invalid Input!")
        self.money += gain
        self.stuff_done += 1
        print(f"Work: {work}\nGained ${gain}")

    def shopping(self):
        print("Shop\n1. Coffee (20$)\n2. Buns (40$)\n3. Cake (500$)\n4. Back")
        try:
            choice = int(input("Enter the choice: "))
        except:
            print("Invalid Input")
            return
        match choice:
            case 1: cost, item = 20, "Coffee" 
            case 2: cost, item = 40, "Buns" 
            case 3: cost, item = 500, "Cake"
            case 4: return
            case _: print("Invalid Input!")
        if self.money < cost:
            print("Insufficient Money!")
            return
        self.money -= cost
        self.stuff_done += 1
        print(f"Bought {item}!")