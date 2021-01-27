# if numbers are different from each other
#class Unique:
#    def all_unique(self, n):
#        num = set()
#        for i in n:
#            if i in num:
#                return "Not Unique"
#            else:
#                num.add(i)
#        return "unique"
#
#
#s = Unique()
#print(s.all_unique([1, 2, 3, 4, 8, 1, 2, 3, 4, 55]))

#Demonstrate how to use Python’s list comprehension syntax to produce
#the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]. 
k = [2 * x for x in range(0, 91)]

alphabets_without_typing_all = [chr(97 + h) for h in range(26)]
print(alphabets_without_typing_all)




