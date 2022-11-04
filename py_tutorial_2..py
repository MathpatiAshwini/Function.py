# Write a Python function to sum all the numbers in a list.

def sum():
    a=[2,9,4,6,7]
    sum=0
    b=[]
    i=0
    while i<len(a):
        sum+=a[i]
        b.append(sum)
        i+=1
    print(b)
sum()