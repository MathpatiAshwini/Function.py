def multiplay():
    a=[1,2,3]
    b=[4,5,6]
    c=[]
    i=0
    while i<len(a):
        k=a[i]*b[i]
        c.append(k)
        i+=1
    print(c)
multiplay()