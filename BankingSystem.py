

class atm:
    def __init__(self):
        self.userMoney = 10000

    def addMoney(self):
        addAmount = input("How much do you want to add: ")
        self.userMoney += int(addAmount)
        print(
            f"You added {addAmount} to your balance. Your new balance is {self.userMoney}")

    def subtrMoney(self):
        subtrInput = input("How much do you want to withdraw: ")
        self.userMoney -= int(subtrInput)
        print(
            f"You withdrew {subtrInput} from your balance. Your new balance is {self.userMoney}")

    def currentBalance(self):
        return self.userMoney

    def askPurpose(self):
        return (input(
            "\nAdd Money: Type 'add' \nWithdraw Money: Type 'withdraw' \nCheck balance: Type 'currbal' \nInput: "))


myBank = atm()
userPurpose = myBank.askPurpose()

if userPurpose == "add":
    myBank.addMoney()
    userPurpose = None

elif userPurpose == "withdraw":
    myBank.subtrMoney()
    userPurpose = None

elif userPurpose == "currbal":
    currBal = myBank.currentBalance()
    print(f"You currently have {currBal} Rs. in your bank")
    userPurpose = None

elif userPurpose == None:
    myBank.askPurpose()

else:
    print('Invalid Input')
