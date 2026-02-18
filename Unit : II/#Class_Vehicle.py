#Class_Vehicle
#Create a base class Vehicle with a method move() and two subclasses Car and Bicycle. Override the move() method in both subclasses. 
#The car should print "Driving on the road" and the bicycle shoudl print "Pedaling on the road". Demonstrate polymorphism by calling 
#the move() method on both objects. 

#Base Class
class Vehicle:
    def Move(self):
        print("The vehicle is moving.")

#Subclass Car
class Car(Vehicle):
    def Move(self):
        print("Driving on the road.")

#Subclass Bicycle
class Bicycle(Vehicle):
    def Move(self):
        print("Pedaling on the road.")

#Demonstrating Polymorphism
Vehicles=[Car(),Bicycle()]

for V in Vehicles:
    V.Move()

