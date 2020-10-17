# Exercise 3: Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of tuple of length two. Do not use the built in function min or max in implementing your solution.

def minmax(data):
    small = large = data[0]
    #large = data[0]
    #if len(data):
    for item in data:
        if item < small:
            small = item
        elif item > large:
            large = item
    return small, large




print(minmax([3, 4, 15, 6, 34, 89, 92, 0, -1]))



