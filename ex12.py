# Pythons random module includes a function choice(data) that return a random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to the builtin range function, that return a random choice from the given range. using only the randrange function, implement your own version of the choice function.
import random

def randomchoice(data):
    return data[random.randrange(0, len(data))]


data = ["Archimedes", "Sena",  "Senadju"]
for k in range(200):
    print(randomchoice(data), end = ' ')








