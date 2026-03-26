'''print (9+9)
print("Python" + "Language")
print ([1,2] + [3,4])

concatenation
-------------
This is nothing but, a (+) behaviour
case-1
------
integers--- this will act as addition for the int

case-2
------
Note : if we access 2 different datatypes we will not get the output.


print("Varun" +[1,2]) #Typeerror
'''

'''Tuple () --->
----------
is a collocation of different datatype and this is represented by (), seperated by (,)
eg...

Thing = (1, "Varun",[12,4],(6,7))
print(Thing)

Thing = (12,98,"Python",(23,"Teja","Python is language" ), (7,8),[8,("pYTHON",[34,9])])
print(Thing)


Num = 9
Num_2  = 90
print (f"before swapping Num = {Num} and Num_2 = {Num_2}")
Num, Num_2 = Num_2, Num
print(f"After swapping Num = {Num} and Num_2  = {Num_2}")
'''

Leap_year = int(input("Enter year: "))
if (Leap_year % 4 == 0 and Leap_year % 100  != 0) or Leap_year % 400 == 0:
       print(f"Yes, {Leap_year} is a Leap year")

else:
    print (f"No, {Leap_year} is not a Leap year")


