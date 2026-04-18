'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::OOPS::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
- - - > Writing Code using Real world concepts that contains both data and functions.
- - - > OOPS are reusable and scannable.
- - - > Reusability -> Write once use many times.
- - - > Sccanability -> Without rewritting everything.
- - - > OOPS is abig concept it has many sub topics but as of now we will now Class, Object and Attributes.
- - - > CLASS : Blueprint or template that defines what kind of data and behaviour a certain type of object will have .
SYNTAX :
class Class_Name:
        Pass
        
- - - > OBJECT : This is instance of class/obj is a real instance create from the class (or) Real thing madefrom blueprint.
SYNTAX :
class Class_Name:
        Pass
object_name = class_name ()
- - - > ATTRIBUTES : These are variables that store data related to a class or object.
SYNTAX :
class Class_Name:
        def __init__(self,arguments) :
                self.arguments = value
object_name = class_name ()
- here each  argument is a attribute, self is the keyword of the constructor init

'#1.  Car-1'
class Car :
         def  __init__(Self, name, model, speed):sss
                 Self.name = name
                 Self.speed = speed
                 Self.model = model

         def display (self) :
                 print(f"{self.name} is model of {self.model} and runs at {self.speed} km/h ")
        
c1 = Car("BMW", 2026, 200)
c2 = Car("AUDI", 2024, 180)

c1.display()
c2.display()


'#2. Dog'

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def display(self):
        print(f"{self.name} is a {self.breed} and is {self.age} years old")

d1 = Dog("Maxi", "Labrador", 2)
d2 = Dog("Choci", "German Shepherd", 5)

d1.display()
d2.display()


'#3. Mobile'

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"{self.brand} {self.model} costs ₹{self.price}")

m1 = Mobile("Apple", "iPhone 15", 80000)
m2 = Mobile("Samsung", "S24", 70000)

m1.display()
m2.display()


'- - - > Constructor (__init__) '
'- - - - - - - - - - - - - - - - - - - - - - - - - - - - '
'- - - > A Constructor is a special method usedn to intiallize object data'
'-  __init__()'









