def natural_sum(n):
    if n==1:
        return 1
    else:
        return (n+natural_sum(n-1))
n=int(input('enter the number'))
x= natural_sum(n)
print(x)
