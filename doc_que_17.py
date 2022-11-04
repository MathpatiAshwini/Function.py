# 7. Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting to be 18. )
def vote():
    a=int(input("enter the valide age:-"))
    if a>=18 :
        print("she is able to vote")
    else:
        print("she is not able to vote")
vote()
