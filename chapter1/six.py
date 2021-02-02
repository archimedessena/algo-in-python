#Exercise 6 Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.

def sum_of_square_of_odd(n):
    t = 0
    y = 0
    for i in range(n):
        if i % 2 == 1:
            j = i * i
            y +=j
            t +=1
        else:
            "Do nothing"
    return y


print(sum_of_square_of_odd(10))


def sums(k):
    return sum(q * q for q in range(1, k) if q % 2 == 1)



print(sums(10))