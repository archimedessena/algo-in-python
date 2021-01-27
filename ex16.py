# In our implementation of the scale function (page 25) the body of the loop executes the command data[j] *= factor. We have discussed that numeric types are immutable, and that use of the *= operator in this contex causes the creation of a new instance (not the mutation of an existing instance). How is it still possible, then that our implementaton of scale changes the actual parameter sent by the caller?

def scale(data, factor):
    for i in data:
        i *= factor
    return data
    



#print("Bad scaling")
#data = [1, 2, 4]; print(data)
#scale(data, 4); print(data)

def realscale(data, factor):
    for i in range (len(data)):
        data[i]*= factor
    return data



v = realscale([1,2,4,5,6,7,8,9,1,2,22,33,44,54], 55)
print(v)