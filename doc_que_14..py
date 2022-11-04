# 14.Write a function to check if a number is prime or not.


def prime_number(n):
    i=1
    count=0
    while i<=n:
        if n%i==0:
            count=count+1
        i+=1
    if count==2:
        print(n,"is a prime")
    elif n==1:
        print(n,"is a prime number")
    else:
        print(n,"not a prime number")
n=int(input("enter the number:"))
prime_number(n)
