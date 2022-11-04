#  Write a function For example, if we give 9119  the function should return 
#   811181, as the  square of 9 is 81 and square of 1  is 1.

def square(a):
    i=0
    while i<len(a):
        e=a[i]
        j=0
        while j<len(e):
            c=int(a[i][j])  
            k=c**2
            j=j+1
        i=i+1
        print(k,end="")
square("9119")