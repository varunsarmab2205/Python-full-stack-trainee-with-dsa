'''
prime_num = int (input("Enter a number: "))6
count = 0
for j in range (1,prime_num+1):
    print(j)
    if prime_num % j == 0 :
        count += 1
        print (count)
if count == 2 :
    print(f"{prime_num} is a prime number ")
else:
    print(f"{prime_num} is a not a prime number ")


for an in range (2,100):
    count = 0
    for j in range (1,an+1):
        if an % j == 0:
            count += 1
    if count == 2:
        print(f"{an} is a prime")
    else:
        print(f"{an} is not  a prime")

list_1 = [1057,197,9,86,17673]

for an in list_1:
    count = 0
    for j in range(1, an + 1):
        if an % j == 0:
            count += 1
    if count == 2:
        print(f"{an} is a prime")
    else:
        print(f"{an} is not a prime")


any = [2,356,8,6,3,2,9]
empty_ = []
for j in  any :
    if j not in empty_:
        empty_.append(j)
print(empty_)


So = int (input("enter any number: "))
length_ = len(str(So))
Amstr_ = 0
for j in str(So):
    Amstr_ += int(j) ** length_
    print(Amstr_)
if Amstr_ == So:
    print(f"{So} is Amstrong num")
else:
     print(f"{So} is not Amstrong num")

'''

'''Task ----- Take a List with only integers and Seperate Even's and Odd's '''









