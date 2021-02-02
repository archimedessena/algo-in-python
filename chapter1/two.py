# Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.

def is_even(k:int):
    assert type(k) == int, "Your input must be an int"
    return (k&1 == 0)
    
    
    
print(is_even(6))

