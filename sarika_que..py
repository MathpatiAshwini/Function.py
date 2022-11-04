def add():
    a=[2,-2,20,25,-18,-65]
    pos=[]
    sum=0
    sum2=0
    neg_sum=[]
    i=0
    while i<len(a):
        if a[i]>0:
            sum2+=a[i]
            pos.append(sum2)
        else:
            sum+=a[i]
            neg_sum.append(sum)
        i+=1
    print(pos)
    print(neg_sum)
add()
