students = {}
def add_student():
    name = input("Enter student name: ")
    mark = float(input("Enter student mark: "))
    students[name] = mark
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
    else:
        for name, mark in students.items():
            print(f"Name: {name}, Mark: {mark}")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
