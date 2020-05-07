# What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?
print(list(range(50,90,10)))












print(list(range(20, 100,5)))


def som(k):
    return sum(t*t for t in range(48, k) if t%3==1)



print(som(48))