class Plane:
    def takeOff(self):
        print("Plane took off")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane has landed")
#takeOff(), fly(), land() --->specialized method (for class plane)
#Here the code has been optimized here as inheritance so the same code can be reused.
'''
there are three types of methods under the context of inheritance
1. Inherited method 2. Overridden method 3. Specialized methods
'''

class CargoPlane(Plane):
    def fly(self):
        print("Plane is flying with goods")
#takeOff(), land() --->inherited method  fly()---> Overridden (for class cargoplane)

class PassengerPlane(Plane):
    def fly(self):
        print("Plane is flying with ppl")
#takeOff(), land(),  --->inherited method  fly()---> Overridden (for class passengerplane)

class FighterPlane(Plane):
    def fly(self):
        print("Plane is flying with weapons")
    def shoot(self):
        print("Plane is shooting bullets")
#takeOff(), land(),  --->inherited method  fly()---> Overridden and shoot() ---> specialized here(for class fighterplane)

# c = CargoPlane()
# f= FighterPlane()
# p = PassengerPlane()
# c.takeOff()
# c.fly()
# c.land()
# p.takeOff()
# p.fly()
# p.land()
# f.takeOff()
# f.fly()
# f.land()
# f.shoot() (Isn't this too long and repetitive?)
'''
We have a solution tho
and that's polymorphism!!
'''
def allowPlane(ref):
    ref.takeOff()
    ref.fly()
    ref.land()
    if isinstance(ref, FighterPlane):
        ref.shoot()
c = CargoPlane()
f= FighterPlane()
p = PassengerPlane()
allowPlane(c)
allowPlane(p)
allowPlane(f)