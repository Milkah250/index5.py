# Base class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must override this method")


# Derived class: Car
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")


# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")


# Derived class: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing on the water 🚤")


# Example usage of polymorphism
def vehicle_action(vehicle):
    vehicle.move()


# Instantiate objects
car = Car()
plane = Plane()
boat = Boat()

# Demonstrate polymorphism
vehicles = [car, plane, boat]
for vehicle in vehicles:
    vehicle_action(vehicle)
