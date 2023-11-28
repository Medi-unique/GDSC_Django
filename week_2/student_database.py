def add_student(database):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    
    database[name] = {"age": age, "grade": grade}
    print("Student added successfully!")


def view_student(database):
    name = input("Enter student name: ")
    if name in database:
        student = database[name]
        print("Student Details:")
        print("Name:", name)
        print("Age:", student["age"])
        print("Grade:", student["grade"])
    else:
        print("Student not found in the database.")


def list_all_students(database):
    print("List of all students:")
    for name, student in database.items():
        print("*************************")
        print("Name:", name)
        print("Age:", student["age"])
        print("Grade:", student["grade"])
        print("*************************")


def update_student(database):
    name = input("Enter student name: ")
    if name in database:
        print("Update student information:")
        age = int(input("Enter new age: "))
        grade = input("Enter new grade: ")

        database[name]["age"] = age
        database[name]["grade"] = grade
        print("Student information updated successfully!")
    else:
        print("Student not found in the database.")


def delete_student(database):
    name = input("Enter student name: ")
    if name in database:
        del database[name]
        print("Student deleted successfully!")
    else:
        print("Student not found in the database.")


def main():
    database = {}

    while True:
        print("****Student Database****")
        print("1. Add Student")
        print("2. View Student")
        print("3. List All Students")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student(database)
        elif choice == "2":
            view_student(database)
        elif choice == "3":
            list_all_students(database)
        elif choice == "4":
            update_student(database)
        elif choice == "5":
            delete_student(database)
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


main()