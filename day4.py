'''
Operators -->An Operator is a symbol that performs an operation on one or more values (operands)and produces a result

Operators are primarily used :
-->Calculate values
-->Compare values / inputs
-->Make decisions
-->Control the program flow

There are major seven categories of Operators in python

-->Arithmetic Operators
-->Assignment Operators
-->Comparision Operators
-->Membership Operators (in, not in )
-->Identity Operators (is, is not)
-->Bitwise Operators
-->Logical Operators
'''

#Arithmetic Operators -->Arithmetic Operators perform Mathematical operators

# +  -->Addition,- -->Subtraction , * -->Multiplication, / -->Division
# ** -->Exponent , % -->Modulus,?? -->Integer Divisor

'''
a=5
b=3
print (a+b)
print (a-b)
print (a*b)
print (a/b) #returns the result in float values 
print (a**b)#returns the exponential value


print(a % b) #Modulus division -->returns remainder
print (a // b) #Integer divison -->returns Quotient discards float 
'''

'''
#f-string notation
num1 = int (input("Enter the first value :"))
num2 = float (input("Enter the second value: "))
result = (num1 + num2)*4
print ("The result is ", result ) #standard notation

#f-string notation
print(f'The result is {result,num1,num2}')
'''

#Assignment Operators
#--> = Assign, += Addition Assignment , -=, %=, //=, **=

'''
a = 4
b = 3
a += 2 #--> a= a+2
print (a)
b += a
print (b)

b //= a
print (b)
'''

#Relational or Comparision Operators --> They always return the boolean
#values (True / False)

# == is equal to, != not equals to
# < less than , > greater than , >= , <=

a = int(input("Enter a value : "))
b = int(input("Enter another value :"))
print (a == b)
print (a != b)
print (a != b)
print (a<b)
print (a>b)
print (a>=b)

#Membership Operators -->They check for the existence of an object in a #collection --> in,not in

'''
a= "codegnan"
print (type(a))
print  ('a' in a)
print ('z' in ''saketh')
print ('z' not in 'codegnan')

b = [12,6,3,4]
c = int (input ("Enter the value "))
print(c)
print(c in b)
print(c not in b)
'''

#Logical Operators --> They are used to combine multiple conditions
#and,or,not

age = int (input ("Enter the age: ")0
vote_right = True
           
'''
print(age>=18 and vote_right)
print (age>18 or vote_right)
print (note vote_right)
'''
#identify operators--> they check the memory location and validate  we used
#(id) function it is different from == operator->  is , is not
'''
a=[1,2,4]
b=[1,2,4]
print(a==b)
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

c  = b
print (c)
print (id(c))
print (c is b) 
'''
#Bitwise Operators --> Bitwise OR | perform bitwise operators we get the result (remember the binary conversion)
print(5 &3)
print(bin(5)) #returns binary numnber




