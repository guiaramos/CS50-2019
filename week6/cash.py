# Modules
from cs50 import get_float

class cash():

    # Getting the info provided
    def __init__(self, amount, paid):

        self.amount = amount
        self.paid = paid

        # Defining coins
        self.coins = {}

        self.coins["Quarters"] = 25
        self.coins["Dimes"] = 10
        self.coins["Nickels"] = 5
        self.coins["Pennies"] = 1

        # Call change
        self.change(self.amount, self.paid)


    # Getting the change
    def change(self, amount, paid):

        change = (paid - amount)*100
        dueChange = {"Quarters":0, "Dimes":0, "Nickels":0, "Pennies":0}

        while True:
            if change >= self.coins["Quarters"]:
                change -= self.coins["Quarters"]
                dueChange["Quarters"] += 1
            else:
                break

        while True:
            if change >= self.coins["Dimes"]:
                change -= self.coins["Dimes"]
                dueChange["Dimes"] += 1
            else:
                break

        while True:
            if change >= self.coins["Nickels"]:
                change -= self.coins["Nickels"]
                dueChange["Nickels"] += 1
            else:
                break

        while True:
            if change >= self.coins["Pennies"]:
                change -= self.coins["Pennies"]
                dueChange["Pennies"] += 1
            else:
                break

        self.show(dueChange)

    # Printing
    def show(self,dueChange):
        print(f"the change is: {dueChange}")


# Start script
userInfo = {}

# Loop for get the correct info
while True:

    amount = get_float("Please, insert the due amount:")
    paid = get_float("Please, insert the amount paid:")

    if amount and paid > 0 and paid > amount:
        userInfo["Amount"] = amount
        userInfo["Paid"] = paid
        break

# Call cash
cash(userInfo["Amount"],userInfo["Paid"])
