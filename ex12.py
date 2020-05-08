# Pythons random module includes a function choice(data) that return a random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to the builtin range function, that return a random choice from the given range. using only the randrange function, implement your own version of the choice function.
import random

def randomchoice(data):
    return data[random.randrange(0, len(data))]


data = [12,34,5,55,78,8]
for k in range(40):
    print(randomchoice(data), end = ' ')







