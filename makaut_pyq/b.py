class A:
    def display(self):
        print("Class A")
class B:
    def show(self):
        print("Class B")
class C(A,B):
    def info(self):
        print("Class C")
obj=C()
obj.display()
obj.show()