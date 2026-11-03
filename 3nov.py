# Example 1:
class A:
    def dispA(self):
        print("A's disp")

class B(A):
    def dispB(self):
        print("B's disp")

b = B()
b.dispA()
b.dispB()

a = A()
a.dispA()
a.dispB()


# Example2
class A:
    def dispA(self):
        print("A's disp")
class B(A):
    def dispB(self):
        print("B's disp")
class C(A):
    def dispC(self):
        print("C's disp")
b = B()
b.dispA()
b.dispB()
b.dispC()  #ATTRIBUTE ERROR: 'B' OBJECT HAS NO ATTRIBUTE DISPC. DID YOU MEAN DISPA?

class A:
    def disp(self):
        print("A's disp")
class B:
    def disp(self):
        print("B's disp")
class C(A,B):
    def dispC(self):
        print("C's disp")

c = C()
c.dispC()
c.disp()