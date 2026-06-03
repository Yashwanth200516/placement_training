class Employee:
    def __init__(self,name,salary):
        self.name=name  #public
        self.__salary=salary #private
        self._dept="IT" #protected

    def get_salary(self):
        return self.__salary
    
    def set_salary(self,amount):
        if amount>0:
            self.__salary=amount
        else:
            print("Invalid salary")
        
    
emp=Employee('Yashwanth',40000)
print(emp.get_salary())
print(emp.name)
emp.set_salary(70000)
print(emp.get_salary())
emp.set_salary(-100)

