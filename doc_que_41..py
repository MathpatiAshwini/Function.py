# Q41. Write a Python program to find the list with maximum and minimum length.
# Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])
def length_of_list():
    a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
    i=0
    count=0
    count2=0
    max=0
    min=a[i]
    while i<len(a):
        n=a[i]
        j=0
        while j<len(n):
            if len(n[j])>max:
                max=n
                count+=1
            elif len(n[j])<min:
                min=n
                count2+=1
            i+=1
    print(max)
    print(min)
    print(count)
    print(count2)
length_of_list()    

