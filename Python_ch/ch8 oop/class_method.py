class person:
    name = "nigga"

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name


p1 = person()
p1.change_name("john")
print(p1.name) # john
print(person.name) #