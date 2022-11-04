# Q42. Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
# The original list is : [15, 81, 11, 234]
def sum_number():
    a=[12,67,98,34]
    i=0
    b=[]
    while i<len(a):
        result=0
        while a[i]>0:
            digit=a[i]%10
            result=result+digit
            a[i]//=10
        b.append(result)
        i=i+1
    print(b)
sum_number()



