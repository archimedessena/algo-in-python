# Demonstrate how to use Pythons list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256]
print([x**2 for x in range(9)]) #[pow(2, x) for x in range(9)]) #square of  the subsequent number


print([2**b for b in range(9)]) # multipling the subsequent number by 2



print([k**3 for k in range(1,8)]) # finding the cube subsequent numbers
print([3**t for t in range(10)])# multipling the subsequent numbers by 3