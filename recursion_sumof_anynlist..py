def sum(mylist): 
    if len(mylist) == 1:  
        return mylist[0] 
    else: 
        return mylist[0] + sum(mylist[1:]) 
         
a=int(input("enter the length"))
i=0
b=[]
while i<a:
    n=int(input("enter the number"))
    b.append(n)
    i+=1 
print(sum(b)) 
