# Base class.
class Vehicle:
    def Vehicle_info(self):
        print("Inside Vehicle class")


# Child class 1.
class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")


# Child class 2.
class SportsCar(Car):
    def sports_car_info(self):
        print("Inside SportsCar class")

if __name__ == "__main__":

    # Create object of SportsCar.
    s_car = SportsCar()

    # Access Vehicle's and Car info using SportsCar object.
    s_car.Vehicle_info()
    s_car.car_info()
    s_car.sports_car_info()
