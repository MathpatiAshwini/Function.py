# Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.

def prime_number(start,end):
    for i in range (start,end+1):
        if i>0:
            for j in range (2,i):
                if i%j ==0:
                    break
            else:
                print(i,end=" ")
start=int(input("enter the starting range:"))
end=int(input("enter the end range:"))
prime_number(start,end)

