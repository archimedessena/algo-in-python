#Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before, and compare this method to an equivalent Python function for doing the same thing.
 
# Go through each of the integers
# Set a variable 
# Push each of the integers to the set variable using a 
# Print the list out

def reverses(arr):
    lean = len(arr)
    leans = [None]*lean
    for i in range(lean):
        leans[lean-1-i] = arr[i]
    return (leans)



d = [2, 4, 6, 8, 10, 12]

print(reverses(d))





# ex14
# Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.




#ex 15
#Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).