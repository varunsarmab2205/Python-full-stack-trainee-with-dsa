''' table_num = int(input("Enter a number: "))
for j in range (1,21) :
    print (f"{table_num} X {j} = {table_num * j}")

    String--- [String is Immutable-can't be modified]
    String is a Sequences of charcaters that are encloseed in quotes ['',"",''' ''']
  Methods:
  Count ()   ,    capitalize ()
  Join  ()   ,    casefold ()
  strip ()   ,    isalnum ()
  replace () ,    isalpha()
  spilt () ,      is digit()

table_num = int(input("Enter a number: "))
for j in range (1,11) :
      print (f"table_num} X {j} = {table_num * j }")

an = "Python IS a Progrmming Language"
count_U = 0
count_L = 0
for ch in an:
    if ch.isupper() :
        count_U += 1
        elif ch.islower() :
        count_L += 1
print(f"There are total {count_U} Cap L")
print(f"There are total {count_L} small L")

an = "Python IS a Programming Language"
Cap_L = []
small_L = []
for ch in an:
    if ch.isupper():
        Cap_L.append (ch)
    elif ch.islower():
        small_L.append(ch)
print(f":{Cap_L} contain all Cap L")
print(f"{small_L} contain all small L")

HDFC_varun_AC_details = {"Name" : "varun", "ATM PIN" : "2205"}
print("Welcome to HDFC  ATM ")
print("Pls insert your ATM")
HDFC_user_pin = input ("Pls enter your 4 digits ATM pin: ")
if len(HDFC_user_pin) == 4:
    if HDFC_user_pin in HDFC_varun_AC_details['ATM PIN']:
        print("The pin correct")
    else:
            print("You have enetered invalid pin")
else:
    print("Pls enter 4 digit pin")'''

per_num = int(input("Enter a number: "))
fact_all = 0
for j in range (1, per_num):
    if per_num % j == 0:
        fact_all += j
if fact_all == per_num:
    print(f"{per_num} is the perfect num")
else:
    print(f"{per_num} is not a perfect num")
    

    
    






  
