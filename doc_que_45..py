# 45. Draw a flowchart to Take 10 numbers as input and create a list of the numbers from the user and update each element of the list according to below rule
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1 
# Sample Input:
# 	23
# 	42 
# 	41 
# 	1
# Sample Output:
# 	-23 
# 	4200 
# 	-41 
# 	-1

def multipal_by():
    a=[23,42,41,1]
    i=0
    while i<len(a):
        if a[i]%2==0:
            print(a[i]*100)
        elif a[i]%2!=0:
            print(a[i]*-1)
        i+=1
multipal_by()


