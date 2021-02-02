# Exercise 1
# Write a short Python function, is_multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and false otherwise
def multiple(x, y):
    if x % y ==0:
        return True
    else:
        False


test = multiple(3, 1)
print(test)