# 46. Draw a flowchart to take a list of N numbers from the user, print True if the complete list consists of consecutive numbers with a difference of one. Print False otherwise. 
# Sample Input:
# 1 2 3 4 5 6 7Sample Output:TrueSample Input:45 46 47 48 49 51 52Sample Output:False
# Sample Input:4 5 6 7 8 9 10Sample Output:TrueSample Input:-5 -6 -7 -8Sample Output:Falseample Input:-3 -2 -1 0 1
# Sample Output:True


def ashu():
    a = [1, 2, 3 ,4 ,5 ,6 ,7]
    i=0
    while i<len(a):
        if a[i]>0:
            k=a[i],a[i]+1
            print(k,"true")
        else:
            p=a[i],a[i]+2
            print(p,"false")
        i+=
ashu()