# Q43.  Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. Print the last 
# ‘N’ elements of the given list. ‘N’ is accepted from the user.
# Sample Input:
# 1
# Sample Output:
# q 
# Sample Input:
# 3
# Sample Output:
# 5
# b 
# q

# def sample():
#     a=['a',1, '2', 5, 'b', 'q']
#     i=0
#     while i<len(a):
#         if i==1:
#             print(a[-1])
#         if i==3:
#             print(a[3:])
#         i+=1
# sample()


# def sample(b):
#     a=['a',1, '2', 5, 'b', 'q']
#     while b<len(a)-1:
#         # print(a[b])
#         b+=1
#     print(a[b])
# sample(1)

def sample(b):
    a=['a',1, '2', 5, 'b', 'q']
    while b<len(a):
        print(a[b])
        b+=1
sample(2)


    
    