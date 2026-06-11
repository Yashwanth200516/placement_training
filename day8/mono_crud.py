from pymongo import MongoClient

client = MongoClient("mongodb+srv://testing:test8055@yashwanth-c.ziy5pcf.mongodb.net/")
db=client["myproject"]

students = db["trail"]

def create_student():
    student = {
        "name": input("Enter student name: "),
        "age": int(input("Enter student age: ")),   
        "course": input("Enter student course: "),
        "email": input("Enter student email: ")
    }
    result = students.insert_one(student)
    print(f"Student created Successfully")
    print(f"Inserted ID: {result.inserted_id}")

def view_students():
    all_students = students.find()
    for student in all_students:
        print(student)

#delete
def delete_student():
    student_id = input("Enter student ID to delete: ")
    result = students.delete_one({"_id": student_id})
    if result.deleted_count > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")

#update
def update_student():
    name = input("Enter student name to update: ")
    new_email = input("Enter new email: ")
    result = students.update_one({"name": name}, {"$set": {"email": new_email}})
    if result.modified_count > 0:
        print("Student updated successfully!")
    else:
        print("Student not found or email is the same.")

while True:
    print("1. Create Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        create_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")