class Person:
    def __init__(self, name,age):
        self.name = name
        self.age=age

    def show_details(self):
        print(f"name:{self.name}\nage:{self.age}")

p1 = Person("Yashwanth",21)
p1.show_details()