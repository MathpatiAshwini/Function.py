def even():
    l=[1,2,3,4,5,6,7,8,9,]
    i=0
    b=[]
    while i<len(l):
        if l[i]%2==0:
            b.append(l[i])
        i+=1
    print(b)
even()



# def chr(a):
#     a='My name Is AsHWINi'
#     i=0
#     count=0
#     count1=0
#     while i<len(a):
#         if a[i].isupper():
#             count+=1
#         if a[i].islower():
#             count1+=1
#         i+=1
#     print("no. of uppercase latter",count)
#     print("no. of lowercase latter",count1)
# (chr('My name Is AsHWINi'))