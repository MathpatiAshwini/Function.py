# bers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).

# def squers():
#     a=int(input("enetr the frist number:"))
#     b=int(input("enter the last number:"))
#     i=0
#     c=[]
#     while i<=b:
#         j=1
#         while j<len(a[i]): 
#             k=a**2
#             c.append(k)
#             j+=1
#         i+=1
#         print(c)
# squers()
   
def printValues():
	l = list()
	for i in range(1,31):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])
printValues()
