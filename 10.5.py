#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways
from random import randint
class Train():
    def __init__(self, trainno):
        self.trainno = trainno
    def book(self, fro, to):
        print(f"The Train Ticket is booked in train {self.trainno} from {fro} to {to}")
    def getstatus(self):
        print(f"The Train no {self.trainno} is running on time")
    def getfair(self, fro, to):
        print(f"The Train fair for train no {self.trainno} from {fro} to {to} is rupees {randint(222,5555)}")

t = Train(11500)
t.book("Bhusawal", "Nardana")
t.getstatus()
t.getfair("Bhusawal", "Nardana")