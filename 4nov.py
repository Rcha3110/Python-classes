class Plane:
    def takeOff(self):
        print("Plane took off")
    def land(self):
        print("Plane has landed")

class CargoPlane(Plane):
    def fly(self):
        print("Plane is flying with goods")

class PassengerPlane(Plane):
    def fly(self):
        print("Plane is flying with ppl")

class FighterPlane(Plane):
    def fly(self):
        print("Plane is flying with weapons")
    def shoot(self):
        print("Plane is shooting bullets")

c = CargoPlane()
f= FighterPlane()
p = PassengerPlane()
c.takeOff()
c.fly()
c.land()
p.takeOff()
p.fly()
p.land()
f.takeOff()
f.fly()
f.land()
f.shoot()