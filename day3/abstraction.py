from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def fuel_type(self):
        pass

    def drive(self):
        print("Driving....")

class Car(vehicle):
    def start_engine(self):
        print("car engine:vroom...")

    def fuel_type(self):
        print("petrol")

class ElectricCar(vehicle):
    def start_engine(self):
        print("electric:slient start")
    
    def fuel_type(self):
        print("charging")

car1=Car()
car1.start_engine()
car1.fuel_type()

car2=ElectricCar()
car2.start_engine()
car2.fuel_type()