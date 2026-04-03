#abstrations
class Car:
    def __init__(self):
        self.acc = True
        self.brk = True
        self.cluthch = True

    def start(self):
        self.acc = True
        self.cluthch = True
        print("car is starting")

car1 = Car()
car1.start()

#encapsulation
