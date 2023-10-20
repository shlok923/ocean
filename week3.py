#----------QUESTION1----------

class Calculator():
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def addition(self):
        return self.n1+self.n2

    def subtraction(self):
        return self.n1-self.n2

    def product(self):
        return self.n1*self.n2

    def division(self):
        if self.n2 == 0:
            return 'No division by 0 around here'
        else:
            return self.n1/self.n2

class Calculator3(Calculator):
    o1 = None
    def __init__(self, n1, n2, n3):
        global o1
        super().__init__(n1, n2)
        self.n3 = n3
        o1 = Calculator(n1,n2)

    def addition(self):
        return o1.addition() + self.n3

    def subtraction(self):
        return o1.subtraction() - self.n3

    def product(self):
        return o1.product() * self.n3

    def division(self):
        if self.n3!=0:
            return o1.division() / self.n3
        else:
            return "Bad boy"
'''
op1 = Calculator(2,3)
print(op1.addition())
print(op1.subtraction())
print(op1.product())
print(op1.division())

op2 = Calculator3(1,2,3)
print(op2.addition())
print(op2.subtraction())
print(op2.product())
print(op2.division())
'''

#----------QUESTION2----------

class Account():
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if (self.balance-amount) > 0:
            self.balance -= amount
        else:
            print("Tumpe to hai hi nau")

    def display_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        self.interest_rate = interest_rate
        super().__init__(account_number, balance)

    def calculate_interest(self):
        #Yearly interest is
        return (self.balance * self.interest_rate * 1)
'''
acc1 = Account(123, 10000)
acc1.deposit(1000)
print(acc1.display_balance())
acc1.withdraw(2000)
print(acc1.display_balance())
acc1.withdraw(100000)

acc2 = SavingsAccount(124, 10000, 0.12)
print('Balance: ',acc1.display_balance())
print('Yearly interest is: ',acc2.calculate_interest())
acc2.deposit(20000)
print(acc2.display_balance())
print('Yearly interest is: ',acc2.calculate_interest())
'''

#----------QUESTION3----------
import random
class Dice():
    def __init__(self, sides:int=6):
        self.sides = sides

    def roll(self):
        return random.randint(1,self.sides+1)
'''
d1 = Dice()
print(d1.roll())
'''

#----------QUESTION4----------

class DiceGame(Dice):
    def __init__(self, num_rolls:int, sides:int, num_dice:int=1):
        self.num_dice = num_dice
        self.num_rolls = num_rolls
        super().__init__(sides)

    def simulate(self):
        outcomes=[]
        for i in range(self.num_rolls):
            out=0
            for j in range(self.num_dice):
                out += self.roll()
            outcomes.append(out)
        return outcomes

d2 = DiceGame(3,6,4)
print(d2.simulate())














