#Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before, and compare this method to an equivalent Python function for doing the same thing.
 
# Go through each of the integers
# Set a variable 
# Push each of the integers to the set variable using a 
# Print the list out




# ex14
# Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.


            
               

#a = [2, 4, 5, 7, 8, 56, 457, 1, 23, 89, 67, 77, 45, 59]
#print(product_odd(a))


            

#ex 15
#Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).

# Ex16:In our implementation of the scale function (page 25), the body of the loop executes the command data[j] = factor. We have discussed that numeric types are immutable, and that use of the = operator in this context causes the creation of a new instance (not the mutation of an existing instance). How is it still possible, then, that our implementation of scale changes the actual parameter sent by the caller?


def scale(data, factor):
    for j in range(len(data)):
          data[j] = factor





# Ex17: Had we implemented the scale function (page 25) as follows, does it work properly?
#def scale(data, factor):
 #   for val in data:
 #       val = factor
#Explain why or why not.






# EX18 Demonstrate how to use Python’s list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].






#ex19 Demonstrate how to use Python’s list comprehension syntax to produce the list [ a , b , c , ..., z ], but without having to type all 26 such characters literally.




#ex20 Python’s random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the elements so that each possible order occurs with equal probability. The random module includes a more basic function randint(a, b) that returns a uniformly random integer from a to b (including both endpoints). Using only the randint function, implement your own version of the shuffle function.







#ex21 Write a Python program that repeatedly reads lines from standard input until an EOFError is raised, and then outputs those lines in reverse order (a user can indicate end of input by typing ctrl-D).




#ex22 Write a short Python program that takes two arrays a and b of length n storing int values, and returns the dot product of a and b. That is, it returns an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . ,n−1.





#ex23 Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If that index is out of bounds, the program should catch the exception that results, and print the following error message: “Don’t try buffer overflow attacks in Python!”



#ex24 Write a short Python function that counts the number of vowels in a given character string.



#ex25 Write a short Python function that takes a string s, representing a sentence, and returns a copy of the string with all punctuation removed. For example, if given the string "Let s try, Mike.", this function would return "Lets try Mike".





#ex26 Write a short program that takes as input three integers, a, b, and c, from the console and determines if they can be used in a correct arithmetic formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”




#ex27 In Section 1.8, we provided three different implementations of a generator that computes factors of a given integer. The third of those implementations, from page 41, was the most efficient, but we noted that it did not yield the factors in increasing order. Modify the generator so that it reports factors in increasing order, while maintaining its general performance advantages.



#ex28 The p-norm of a vector v = (v1,v2, . . . ,vn) in n-dimensional space is defined as v = p  vp 1 +vp 2 +· · ·+vp n . For the special case of p = 2, this results in the traditional Euclidean norm, which represents the length of the vector. For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a Euclidean norm of √ 42+32 = √ 16+9 = √ 25 = 5. Give an implementation of a function named norm such that norm(v, p) returns the p-norm value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers.




# Projects
#ex29 Write a Python program that outputs all possible strings formed by using the characters c , a , t , d , o , and g exactly once.




#ex30 Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2.





#ex31 Write a Python program that can “make change.” Your program should take two numbers as input, one that is a monetary amount charged and the other that is a monetary amount given. It should then return the number of each kind of bill and coin to give back as change for the difference between the amount given and the amount charged. The values assigned to the bills and coins can be based on the monetary system of any current or former government. Try to design your program so that it returns as few bills and coins as possible.





#ex32 Write a Python program that can simulate a simple calculator, using the console as the exclusive input and output device. That is, each input to the calculator, be it a number, like 12.34 or 1034, or an operator, like + or =, can be done on a separate line. After each such input, you should output to the Python console what would be displayed on your calculator.






#ex33 Write a Python program that simulates a handheld calculator. Your program should process input from the Python console representing buttons that are “pushed,” and then output the contents of the screen after each operation is performed. Minimally, your calculator should be able to process the basic arithmetic operations and a reset/clear operation.





#ex34 A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program that will write out the following sentence one hundred times: “I will never spam my friends again.” Your program should number each of the sentences and it should make eight different random-looking typos.





#ex35 The birthday paradox says that the probability that two people in a room will have the same birthday is more than half, provided n, the number of people in the room, is more than 23. This property is not really a paradox, but many people find it surprising. Design a Python program that can test this paradox by a series of experiments on randomly generated birthdays, which test this paradox for n = 5,10,15,20, . . . ,100.






#36 Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word appears in the list. You need not worry about efficiency at this point, however, as this topic is something that will be addressed later in this book.