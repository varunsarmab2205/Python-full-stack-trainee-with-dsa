#Password Strength Checker

print(" Welcome to Password Strength Checker\n")

password = input("Enter your password: ")

#Conditions
length = len(password)

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

print("\nChecking password strength...\n")

# Decision making
if length < 6:
    print("Weak Password (Too short)")
elif length >= 6:
    if has_upper and has_lower and has_digit and has_special:
        print("Strong Password")
    elif has_upper and has_digit:
        print("Medium Password")
    else:
        print("Weak Password")

print("\nTip: Use mix of uppercase, numbers & symbols for strong password 🔐")
