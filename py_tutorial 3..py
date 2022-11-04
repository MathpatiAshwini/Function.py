# Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
def multiply():
    a=[8, 2, 3, -1, 7]
    i=1
    sum=0
    while i<len(a):
        k=a[i]**2
        sum=k
        i+=1
        print(sum)
multiply()