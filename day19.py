'''a = [3,4,5]
b = [3,4,5]
c = a
print(a is c)

num = int(input("enter the number"))
for i in range(1,num):
    if  1 % num == 0 :
        sum += 1
        if sum == 2:
           print("Not prime number")
        else:
          print("prime numnber")
       
 '''
'''Dict-
variavble and rules-
and or logical examples
continue and break
fibonacci
prime
palindrome


Dict-- key value pair
key- unique , value can be (list,int), ex: name = varun

variable - to store data, rules -

and - both conditions are true or false , or - any one condition must be true

range()- used mainly in loops to idetify sequence of integers in iteration

'''

#fibonacci

num = int(input("enter a number:"))
num=0
n1=0
n2=1
for i in range(num+1):
              n3 = n1+n2
              n1 = n2
              n2 = n3
              print(n3)
   


          


