# Demonstrate how to use Pythons list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

def sum_increase_two():
    a = 0
    factor = 0
    while True:
        yield  a
        factor += 1
        a += 2*factor
       

good = sum_increase_two()
[next(good) for _ in range(10)]
print(good)




