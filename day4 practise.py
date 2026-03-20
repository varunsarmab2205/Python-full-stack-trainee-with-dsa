print(" Welcome to Smart Billing System\n")

name = input("Enter customer name: ")
amount = float(input("Enter total purchase amount: "))

# Applying discount using conditional statements
if amount >= 5000:
    discount = 20
elif amount >= 3000:
    discount = 15
elif amount >= 1000:
    discount = 10
else:
    discount = 5


# Operators used here
discount_amount = (discount / 100) * amount
final_amount = amount - discount_amount

# Output
print("\n BILL SUMMARY")
print("Customer:", name)
print("Original Amount:", amount)
print("Discount Applied:", discount, "%")
print("Discount Amount:", discount_amount)
print("Final Amount to Pay:", final_amount)

# Logical operator usage
if amount > 5000 :
    print(" You unlocked VIP customer status!")

print("\n Thank you for shopping with us!")
