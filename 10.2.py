#Write a class “Calculator” capable of finding square, cube and square root of a number.
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

a = calculator(n)
a.square()
a.cube()
a.squareroot()