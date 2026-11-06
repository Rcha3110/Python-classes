class OS:
    def __init__(self):
        print("Os is created")
    def checkOS(self):
        print("Os is working")
class Charger:
    def __init__(self):
        print("Charger is created")
    def checkCharger(self):
        print("Charger is working")
class Mobile:
    def __init__(self):
        self.s = OS()
        print("Mobile is created")
    def checkMobile(self):
        print("Mobile is working")
    def hasA(self, c):
        print("Charger connected to mobile")

m = Mobile()
c = Charger()
m.hasA(c)
m.checkMobile()
c.checkCharger()
m.s.checkOS()
del m #or m = None
c.checkCharger()
# m.checkMobile() #NameError: name 'm' is not defined
# m.s.checkOS()  #NameError: name 'm' is not defined

#--------------- Abstraction Example -----------------------------------------------
#Why do we need abstract class if all the child class already has the method and will execute them themselves?
#Wouldn't they execute their methods themselves instead of inheriting from the Plane class?
from abc import ABC, abstractmethod
class Plane(ABC):
    @abstractmethod
    def takeOff(self):
        pass #print("Plane took off") since none children are using this implementation
    @abstractmethod
    def fly(self):
        pass #print("Plane is flying")
    @abstractmethod
    def land(self):
        pass #print("Plane has landed")
class CargoPlane(Plane):
    def takeOff(self):
        print("Cargo Plane took off to low altitude")
    def fly(self):
        print("Cargo Plane is flying with goods")
    def land(self):
        print("Cargo Plane has landed @60kmph")
class PassegnerPlane(Plane):
    def takeOff(self):
            print("Passenger Plane took off to medium altitude")
    def fly(self):
        print("Passenger Plane is flying with people")
    def land(self):
        print("Passenger Plane has landed @100kmph")
class FighterPlane(Plane):
    def takeOff(self):
            print("Fighter Plane took off to high altitude")
    def fly(self):
        print("Fighter Plane is flying with weapons")
    def land(self):
        print("Fighter Plane has landed @200kmph")
def allowPlane(ref):
    ref.takeOff()
    ref.fly()
    ref.land()
c = CargoPlane()
p = PassegnerPlane()
f = FighterPlane()
allowPlane(c)
allowPlane(p)
allowPlane(f)