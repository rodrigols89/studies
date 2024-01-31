# Base class.
class Vehicle:
    def Vehicle_info(self):
        print("Inside Vehicle class")


# Child class.
class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")


if __name__ == "__main__":

    # Create object of Car.
    car = Car()

    # Access Vehicle's info using car object
    car.Vehicle_info()
    car.car_info()
