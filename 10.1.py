#Create a class “Programmer” for storing information of few programmers,working at Microsoft


class Programmer():
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary =salary
        self.pin = pin

a = Programmer("Sanket", 120000, 425201)
print(a.name, a.salary, a.company, a.pin)