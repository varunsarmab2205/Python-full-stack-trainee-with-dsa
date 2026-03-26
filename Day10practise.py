#List to store student records (each student is a tuple)
students = []

while True:
    print("\n--- Student Record Manager ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Find Topper")
    print("5. Exit")

    choice = input("Enter choice: ")

    #Add Student
    if choice == "1":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        
        student = (name, marks)   # tuple
        students.append(student)  # add to list
        
        print("Student added successfully!")

    #View Students
    elif choice == "2":
        if len(students) == 0:
            print("No records found.")
        else:
            print("\nStudent List:")
            for s in students:
                print("Name:", s[0], "| Marks:", s[1])

    # Search Student
    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False

        for s in students:
            if s[0].lower() == search_name.lower():
                print("Found -> Name:", s[0], "| Marks:", s[1])
                found = True
                break

        if not found:
            print("Student not found.")

     #Find Topper
    elif choice == "4":
        if len(students) == 0:
            print("No data available.")
        else:
            topper = students[0]

            for s in students:
                if s[1] > topper[1]:
                    topper = s

            print("Topper is:", topper[0], "with", topper[1], "marks")

    #Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
