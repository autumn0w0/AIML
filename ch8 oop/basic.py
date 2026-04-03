# class Student:
#     name = "autumn"

# s1 = Student()
# print(s1.name)  # autumn 

class Student:
    def __init__(self, fullname):
        self.name = fullname

s1 = Student("autumn")
print(s1.name)  # autumn