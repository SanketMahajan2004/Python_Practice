
n = int(input("Enter the number :"))
class calculator():
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"Square is {self.n*self.n}")
    def cube(self):
        print(f"Cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"Squareroot is {self.n**1/2}")
    @staticmethod
    def greet():
        print("Hello")

a = calculator(n)
a.square()
a.cube()
a.squareroot()
a.greet()