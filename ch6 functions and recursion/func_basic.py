def sun(a, b): 
    s = a + b
    return s
print(sun(3, 4))

def avg_of_3_num(a, b, c):
    s = a + b + c
    avg = s / 3
    return avg
print(avg_of_3_num(3, 4, 5))

#predefined parameter
def sum(a=1, b=2): 
    s = a + b
    return s
print(sum())