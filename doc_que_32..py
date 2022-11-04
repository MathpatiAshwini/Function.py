# Q32.Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n (inclusive). 
# n=0 == >[1]   #[2^0]
# n = 1  ==> [1, 2]     # [2^0, 2^1]
# n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2].
        
def non_negative():
    a=int(input("enter the number:-"))
    i=1
    b=[]
    while i<=a:
        k=a*i
        b.append(k)
        i+=1
    print(b)
non_negative()
        