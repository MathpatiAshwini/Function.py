def table(n,i):
    if i>10:
        return
    else:
        print(n,"*",i,"=",n*i)
        return(table(n,i+1))
       
n=int(input("enter the number"))
table(n,1)
