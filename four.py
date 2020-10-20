# Exercise 4: Write a Python function that takes a positive integer n and returns the sum of the squares of all positive integers smaller than n.   
def square(n):
    t = 0
    y = 0
    for i in range(n):
        j = i * i
        y +=j
        t +=1
    return y


print(square(2))




def simple(k):
    return sum(t*t for t in range(1, k))


print(simple(2))