class student:
    clg_name = "LPU"
    name = "autumn"

    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
        print("constructor called")

s1 = student("autumn", 90)
print(s1.name, s1.marks)  # autumn 90