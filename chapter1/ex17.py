# Had we implented the scale function (page 25) as follows, does it work properly? Explain your answer
def scale(data, factor):
    for val in data:
        val *= factor
