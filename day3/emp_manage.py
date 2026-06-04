class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        print("-" * 20)


employees = []

while True:
    print("\nEMPLOYEE MANAGEMENT SYSTEM")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = int(input("Enter Salary: "))

        emp = Employee(emp_id, name, department, salary)
        employees.append(emp)

        print("Employee Added Successfully!")

    elif choice == 2:
        if len(employees) == 0:
            print("No employees found.")
        else:
            for emp in employees:
                emp.display()

    elif choice == 3:
        search_id = input("Enter Employee ID to search: ")

        found = False
        for emp in employees:
            if emp.emp_id == search_id:
                emp.display()
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == 4:
        update_id = input("Enter Employee ID: ")

        found = False
        for emp in employees:
            if emp.emp_id == update_id:
                new_salary = int(input("Enter New Salary: "))
                emp.salary = new_salary
                print("Salary Updated Successfully!")
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == 5:
        delete_id = input("Enter Employee ID: ")

        found = False
        for emp in employees:
            if emp.emp_id == delete_id:
                employees.remove(emp)
                print("Employee Deleted Successfully!")
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")