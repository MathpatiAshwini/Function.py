def check_numbers(a,b):
    for i in range(len(a)):
        if(a[i]%2==0 and b[i]%2==0):
            print("both are even")
        else:
            print("both numbers are not even")
l1=[10,20,22]
l2=[16,18,10,30,20]
check_numbers(l1,l2)
