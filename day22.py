'''
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::RECURSIVE FUNCTIONS:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

It is technique where function calls directly or indirectly to solve a problem by breaking into smaller , simpler subproblems, it is
used when  a problem can be divided into subtasks.


def validate_pin(self) :
    while self.remaining_attempts > 0 :
        user_pin = input ("Enter 4 digit pin: ")
        if len(user_pin) == 4 and user_pin == self.user_information:
              print("Welcome to Varun ATM")
              return True
        else:
                 self.remaining_attenpts  -= 1
                 if self.remiaining_attempts > 0:
                        print (f' Invalid pin: {self.remiaining_attempts}')
                else:
                        print("Card blocked. Please contact customer care)
                    return False

                   

':::::::::::::::::::::::::::::::::::::;;:::::::::::::::::::::::::::VOWELS AND CONSONANTS::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
me = input("Enter the string: ")
vowel_list=[]
consonents_list = []
def vowel(me,vowel_list,consonents_list):
        for j in me :
               if  j in "AEIOUaeiou":
                   vowel_list.append(j)
               else:
                   consonents_list.append(j)
        print(f'{vowel_list} these are all vowel in the string')
vowel(me, vowel_list,consonents_list)

':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Varun Atm:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'''

hdfc_details={"name" : "varun", "pin" : "2205","balance":12000}
print("welcome to hdfc bank")
print("enter the atm card")
hdfc_pin=input("enter the 4 digit pin: ")
if len(hdfc_pin) == 4:
    if hdfc_pin in hdfc_details["pin"]:
        user_choice=int(input("Enter \n1.withdraw: \n2.deposite : "))
        if user_choice == 1:
            amount_w= int(input("Enter the amount you want to withdraw: "))
            if amount_w <= hdfc_details['balance']: 
               hdfc_details['balance'] -= amount_w
               print(f"money withdrawn ,your balance is {hdfc_details['balance']}")
            else:
                print("insufficient funds")
        elif user_choice == 2:
            depositemoney=int(input("enter the amount you want to deposite:"))
            if depositemoney % 100 == 0 and depositmoney>=5000:
                hdfc_details['balance'] += depositemoney
                print(f"you have deposited {depositemoney} so the balance is {hdfc_details['balance']}")
            else:
                 print(f"you have deposited {depositemoney} is a change or less than 5000, which you can not deposit")
    else:
        print("you have entered wrong pin")
else:
    print("invalid pin , enter 4 digit pin")




