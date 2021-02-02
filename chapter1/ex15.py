# Write a python function that takes a sequence of numbers and determines if all the numbers are different from each other(that is they are distinct)

def distinct(n):
    num = set()
    for i in n:
        if i in num:
            return "Numbers are not unique."
        else:
            num.add(i)
    return "Numbers are unique."
        

b = distinct([2, 3, 4, 5, 6, 7, 8, 2])
print(b)

