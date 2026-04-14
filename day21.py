'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::WAYS TO PASS ARGUMENTS IN A CALLING FUNCTION::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'''REQUIRED ARGUMENTS
------------------------------
n = 95
n2 = 10
def add (n, n2) :
    print(n+n2)
add (n, n2)   'in calling function the number of arguments should match with the keyword arguments , or else we will get error'

 
name = "varun"
def sum_num(name):
    print(name)
sum_num(name = "Guru")
sum_num(name = "varun")  'these are used for reusability , if we use the calling function after n number of lines still we get the output'

'EVEN OR ODD'

n1 = 147
def even(n1):
    if n1%2 == 0:
        print(f'{n1} is even num')
    else:
        print(f'{n1} is odd num')
even(n1)


'''

'PRIMIE NUMBER'

def prime(num, count) :
    for i in range (1, num+1):
        if num%i == 0 :
               count+=1
    if count==2:
            print(f'{num} is a prime')
    else:
            print(f'{num} is not prime')

while(1) :
           prime(num=int(input("Enter a number: ")),count=0)
           


def any (num, num_3, num_2) :
     print (f"num = {num}, num_2= {num_2}, num_3= {num_3}")
any(num_2=7, num=0,  num_3 = 90) 

