class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):
    def show(self):
        super().show()  # Calls show() of first parent in MRO
        print("Class C")

c = C()
c.show()