def sum_of_multiplyes():
    i=0
    sum=0
    while i<m:
        if i%n==0:
            sum=sum+i
        i+=1
    print(sum)
n=int(input("enter the number"))
m=int(input("enter the number"))
sum_of_multiplyes()
