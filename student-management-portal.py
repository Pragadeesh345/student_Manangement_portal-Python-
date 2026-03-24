students = []

while True:

    print("1 Add student")
    print("2 Show students")
    print("3 Search student")
    print("4 Delete student")
    print("5 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        students.append(name)
        print("Student added")

    elif choice == 2:
        if len(students) == 0:
            print("No students")
        else:
            print("Student list:")
            for i in students:
                print(i)

    elif choice == 3:
        name = input("Enter name to search: ")

        found = 0

        for i in students:
            if i == name:
                found = 1

        if found == 1:
            print("Student found")
            print(i)
        else:
            print("Student not found")

    elif choice == 4:
        name = input("Enter name to delete: ")

        if name in students:
            students.remove(name)
            print("Deleted")
        else:
            print("Not found")

    elif choice == 5:
        print("Exiting")
        break

    else:
        print("Invalid choice")
