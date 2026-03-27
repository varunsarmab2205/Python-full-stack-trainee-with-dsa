#Sri Rama Navami Devotional Assistant

print(" Welcome to Sri Rama Navami Devotional Assistant \n")

#Tuple (festival info)
festival_info = ("Sri Rama Navami", "SRI RAMA & SITA DEVI" , "Ayodhya")

#List (menu options)
menu = [
    "1. View Festival Info",
    "2. Read Sloka",
    "3. View Prasadam List",
    "4. Listen Story (Text)",
    "5. Exit"
]

# List of prasadam items
prasadam = ["Pulihora", "Panakam", "Vadapapu", "Chalimidi"]

#Sloka (string)
sloka = "JAI SITARAM"

#Story (string)
story = "Lord Rama, the seventh avatar of Vishnu, was born in Ayodhya to King Dasharatha and Queen Kaushalya."

while True:
    print("\n Menu:")
    for item in menu:
        print(item)
    
    choice = input("\nEnter your choice: ")

    # Conditional statements
    if choice == "1":
        print("\n Festival Info:")
        print("Festival:", festival_info[0])
        print("Gods:", festival_info[1])
        print("Place:", festival_info[2])

    elif choice == "2":
        print("\n️ Sloka:")
        print(sloka)

    elif choice == "3":
        print("\n Prasadam Items:")
        for item in prasadam:
            print("-", item)

    elif choice == "4":
        print("\n Story:")
        print(story)

    elif choice == "5":
        print("\n JAI SITARAM! Happy Sri Rama Navami!")
        break

    else:
        print("\n Invalid choice. Try again!")
