from dbconnect import connect_db
def add_student():
    conn = connect_db()

    if conn is None:
        print("Unable to connect to database")
        return

    cursor = conn.cursor()

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    gender = input("Enter gender: ")
    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    course = input("Enter course: ")
    department = input("Enter department: ")
    address = input("Enter address: ")

    query = """
    INSERT INTO students
    (
        first_name,
        last_name,
        gender,
        date_of_birth,
        email,
        phone,
        course,
        department,
        address
    )
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        first_name,
        last_name,
        gender,
        date_of_birth,
        email,
        phone,
        course,
        department,
        address
    )

    cursor.execute(query, values)
    conn.commit()

    print("Student added successfully!")

    cursor.close()
    conn.close()

def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()
    for student in students:
        print(student)
    cursor.close()
    conn.close()

def update_student():
    conn = connect_db()
    if conn is None:
        print("Unable to connect to the database.")
        return

    cursor = conn.cursor()
    student_id = input("Enter the student ID to update: ").strip()
    if not student_id.isdigit():
        print("Student ID must be a number.")
        cursor.close()
        conn.close()
        return

    allowed_fields = {
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
        "email",
        "phone",
        "course",
        "department",
        "admission_date",
        "address",
    }
    update_field = input(
        "Enter the field to update (first_name, last_name, gender, date_of_birth, email, phone, course, department, admission_date, address): "
    ).strip()

    if update_field not in allowed_fields:
        print("Invalid field name.")
        cursor.close()
        conn.close()
        return

    new_value = input("Enter the new value: ").strip()
    query = f"UPDATE students SET {update_field} = %s WHERE student_id = %s"
    values = (new_value, int(student_id))
    cursor.execute(query, values)
    conn.commit()
    print("Student updated successfully!")
    cursor.close()
    conn.close()


def delete_student():
    conn = connect_db()
    if conn is None:
        print("Unable to connect to the database.")
        return

    cursor = conn.cursor()
    student_id = input("Enter the student ID to delete: ").strip()
    if not student_id.isdigit():
        print("Student ID must be a number.")
        cursor.close()
        conn.close()
        return

    query = "DELETE FROM students WHERE student_id = %s"
    values = (int(student_id),)
    cursor.execute(query, values)
    conn.commit()
    print("Student deleted successfully!")
    cursor.close()
    conn.close()
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":                 
        print("thank you")
        break
    else:
        print("Invalid choice. Please try again.")