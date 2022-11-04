def  greater (a,b):
    if  a>b:
        return a
    else:
        return b
def greatest (a,b,c):
    if greater(a,b)>c:
        return greater(a,b)
    else:
        return c
print(greatest(12,10,19))