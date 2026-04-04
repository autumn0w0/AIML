#abstrations
# class Car:
#     def __init__(self):
#         self.acc = True
#         self.brk = True
#         self.cluthch = True

#     def start(self):
#         self.acc = True
#         self.cluthch = True
#         print("car is starting")

# car1 = Car()
# car1.start()

#inheritance
class Car:
    @staticmethod
    def start():
        print("car is starting")
    
    @staticmethod
    def stop():
        print("car is stopping")

class Bmw(Car):
    def __init__(self, model):
        self.model = model

car1 = Bmw("X5")
print(car1.model) # X5
car1.start() # car is starting