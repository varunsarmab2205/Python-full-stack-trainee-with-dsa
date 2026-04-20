'''
class BankAC:
    def __init__(self,balance):
        self.__balance = balance

    def deposite(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
Acc = BankAC(15000)
Acc.deposite(17000)
print(Acc.get_balance())

':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::INHERITANCE::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'- - - > This allows a child class (subclass) to acquire the attributes and methods of a parent class (Base class) this is also called child class.'

'''

class Father :
        def skill_1(self) :
              print("Father: hard working")

class Mother :
        def skill_2(self) :
               print("Mother: Cooking")

class Child(Father, Mother) :
        def All_skills(self) :
              print("Father: hard working")


    
