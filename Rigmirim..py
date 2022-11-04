def all():
    a=int(input("enter the length"))
    i=0
    b=[]
    while i<a:
        n=int(input("enter the number"))
        b.append(n)
        i+=1
    return b
def even_odd():
    ar=all()
    i=0
    while i<len(ar):
        if ar[i]%2==0:
            print(ar[i],'is even')
        else:
            print(ar[i],'is odd')
        i+=1
even_odd()
