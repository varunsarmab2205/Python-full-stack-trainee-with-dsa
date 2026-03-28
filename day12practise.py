#Smart Contact Book 

contacts = {}

while True:
    print(" Contact Book ")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

#Add Contact
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")

        if name in contacts:
            print("Contact already exists!\n")
        else:
            contacts[name] = (phone, email)
            print("Contact Added!\n")

#View Contacts
    elif choice == "2":
        if contacts == {}:
            print("No Contacts Found\n")
        else:
            for name in contacts:
                print("Name:", name)
                print("Phone:", contacts[name][0])
                print("Email:", contacts[name][1])
                print()

    # Search Contact
    elif choice == "3":
        search = input("Enter name to search: ")

        if search in contacts:
            print("Found Contact!")
            print("Name:", search)
            print("Phone:", contacts[search][0])
            print("Email:", contacts[search][1])
        else:
            print("Contact Not Found\n")

#Delete Contact
    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Deleted Successfully\n")
        else:
            print("Contact Not Found\n")

#Exit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice\n")
