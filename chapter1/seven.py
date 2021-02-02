# Give a single command that computes the sum from ex6, relying on Pythons comprehension syntax and the built in sum function


def sum_of_square_odds(t):
    return sum(k * k for k in range(1, t) if k % 2 ==1)


print(sum_of_square_odds(5))


