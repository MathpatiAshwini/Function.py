# def sum_of_numbers(limit):
#     a=int(input("enter the frist number:-"))
#     b=int(input("enter the second number:-"))
#     i=1
#     sum=0
#     while i<=limit:
#         k=a*i
#         p=b*i
#         print(k,p)
#         i+=1
# sum_of_numbers(10)

def sum_of_numbers(limit):
    a=int(input("enter the frist number:-"))
    b=int(input("enter the second number:-"))
    i=1
    sum=0
    while i<=limit:
        k=a*i
        p=b*i
        sum+=k+p
        print(sum,end=" ")
        i+=1
sum_of_numbers(10)