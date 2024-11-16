# Defining the base class Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Defining the Car class that inherits Vehicle
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Defining the Plane class that inherits Vehicle
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Creating instances of Car and Plane
car = Car()
plane = Plane()

# Calling the move method on both objects
print(car.move())  # Output: Driving 🚗
print(plane.move())  # Output: Flying ✈️
