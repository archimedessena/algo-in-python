# Write a short python function that takes a sequence of integers values and determines if there is a distinct pair of numbers in the sequence whose product is odd.
def pair_odd(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] != data[j] and data[i] * data[j] % 2 ==1:
                print (data[i], data[j])






d = [ 2, 3, 5, 6, 7]
print(pair_odd(d))
