# Q12.Numbers ending with zeros are boring.They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105

def remove_no():
    a=int(input("enter the length"))
    b=[]
    i=0
    while i<a:
        x=int(input("enter the number"))
        b.append(x)
        num=b[i]
        n=num*1
        r=num%1000
        m=r%100
        y=m%10
        i=i+1
    print('"',n-r,"+",r-m,"+",m-y,"+",y,'"')
remove_no()