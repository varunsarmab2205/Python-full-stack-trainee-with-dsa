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
'''
'#1.  Car-1'
class Car :
         def  __init__(Self, name, model, speed):
                 Self.name = name
                 Self.speed = speed
                 Self.model = model

         def display (self) :
                 print(f"{self.name} is model of {self.model} and runs at {self.speed} km/h ")
        
c1 = Car("BMW", 2026, 200)
c2 = Car("AUDI", 2024, 180)

c1.display()
c2.display()
