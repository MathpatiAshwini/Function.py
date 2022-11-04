# .Write a Python function to find the Max of three numbers.
def max_two(a,b):
    if a>b:
        return a
    return b
def max_three(a,b,c):
    return max_two(a,max_two(b,c))
print(max_three(-43,-60,-5))


