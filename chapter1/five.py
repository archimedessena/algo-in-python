# Exercise 5: Give a single command that computes the sum from Exercise 1.4, relying on Python`s comprehension syntax and the built in sum function.
def single_command(n):
    return sum(m * m for m in range(1, n))

