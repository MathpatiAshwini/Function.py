def Total_sum(a,k):
    
    s = 0
    
    while(k > 0):
        
        r = k % 10
        
        s += (r**a)         
        
        k //= 10
    
    return s                  
    
def Number_of_digits(num):      
    c = 0
    
    while (num>0):
        
        c+=1
        
        num//=10
    
    return c
def isArmstrong(n):
    
    k = n
    
    a = Number_of_digits (k)         
    
    sum_of_digits = Total_sum (a,k)  
    if (sum_of_digits == n):
        
        return True
    
    return False
    
    
    
a = int(input("Enter the lower range  :"))
b = int(input("Enter the higher range :"))
print ("The Armstrong numbers in the given range",a, "and",b,"are")
for i in range(a,b+1):
    
    if(isArmstrong(i)):
        print (i)
