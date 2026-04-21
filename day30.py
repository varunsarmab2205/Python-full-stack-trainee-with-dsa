''''::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Multi Level::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
' - - - - - - - - - - - - - - - - - - - - - - - - - '
' "This occurs when a class inherits from a child class , creating a grandparent - - > parent - - > child in this structure" '



#classes

class Grandparent:
       def Show_Grandparent(self)
              print("I am Grandaparent")

class Parent(Grandparent) :
       def Show_Parent (self):
              print("I'm Parent")

class child(Parent) :
       def Show_child(self):
              print ("I'm child")

any = child ()
any.Show_GrandParent ()
any.Show_Parent ()
any.Show_child ()


# 1. Manager name, skills, salary team size

class Person:
    def __init__(self, name):
        self.name = name

    def skills(self):
        print(f"{self.name} has basic communication skills")


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def job(self):
        print(f"{self.name} works in  Capegemini and earns {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def manage(self):
        print(f"{self.name} manages a team of {self.team_size} members")


m = Manager(input('Enter name: '), int(input('Enter Salary: ')),int(input('Enter Team size: ')))

m.skills()
m.job()
m.manage()

'''

'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::HYBRID INHERITENCE::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;'
' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
' - - - - - > When we use twoor more types of inheritance in a single class then it is called hybrid inheritance'

#HIERARCHIAL INHERITANCE======================================================================================
#This occurs when multiple child classes inherit from a single parent class ,this process is called hierarchial
'''
class parent:
    def par(self):
        print("I am parent")
class child1(parent):
    def chi(self):
        print("I am first child")
class child2(parent):
    def chil(self):
        print("I am second child")
class child3(child1,child2):
    def dis(self):
        print("I am the child")
gene = child3()
gene.par()
gene.chi()
gene.chil()
gene.dis()
'''
#HYBRID INHERITANCE=========================================================================================
#when we use two or more types of inheritance in a single class then it is called hybrid inheritance
'''
class parent:
    def par(self):
        print("I am parent")
class child1(parent):
    def chi(self):
        print("I am first child")
class child2(parent):
    def chil(self):
        print("I am second child")
class child3(child1,child2):
    def dis(self):
        print("I am the child")
gene = child2()
llm = child1()
llm.par()
gene.par()
'''



class Grandparent:
    def Show_GrandParent(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def Show_Parent(Self):
        print("I am parent")
        
class Child(Parent):
    def Show_child(self):
        print("I am child")


class library:
    def show_books(self):
        print("we are having 2500 books in our library")

class librarian(library):
    def showdetails(self):
        print("you are have 250/- penality")

class user(librarian):
    def show(self):
        print("i will clear the penality , and i want artificial neural network book ")

class hybrid(Child,user):
    def hi(self):
        print("I am hybrid class")

hello=hybrid()
hello.Show_GrandParent()
hello.Show_Parent()
hello.Show_child()
hello.show_books()
hello.showdetails()
hello.show()
hello.hi()

