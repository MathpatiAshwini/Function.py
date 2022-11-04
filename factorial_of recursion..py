def factorial_number(n):
    if n==1:
        return 1
    else:
        return (n*factorial_number(n-1))
x= factorial_number(5)
print(x)