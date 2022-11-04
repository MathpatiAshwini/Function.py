def tab_rec_fun(n, i):
    if(i>10):
        return
    else:
        print(n, "*", i, "=", n*i)
        return tab_rec_fun(n, i+1)

n = int(input("Enter the Number: "))
tab_rec_fun(n, 1)
