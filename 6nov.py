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
m.checkMobile() #NameError: name 'm' is not defined
m.s.checkOS()  #NameError: name 'm' is not defined
