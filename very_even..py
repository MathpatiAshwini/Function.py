def very_even():
    n=int(input('enter the number'))
    i=0
    a=n
    sum=0
    while n>0:
        r=n%10
        sum=sum+r
        n//=10
        i+=1
    print(sum)
    if n%2==0:
        if sum%2==0:
            print(a,'is very even number')
        else:
            print(a,'not a very even number')
very_even()