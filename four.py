# Exercise 4: Write a Python function that takes a positive integer n and returns the sum of the squares of all positive integers smaller than n.   
def square(data):
    result = 0
    for val in range(data):
        result = val**2 + result
        result += 1
    return result

print(square(3))




