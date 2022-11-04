def calculator(number_x,number_y,operation):
    l=[]
    if(operation=="add"):
        print(number_x+number_y)
    elif(operation=="sub"):
        print(number_x-number_y)
    elif(operation=="divide"):
        print(number_x/number_y)
    elif(operation=="multiply"):
        pass
    for i in range(len(number_x)):
        mul=number_x[i]*number_y[i]
        l.append(mul)
        print(l)
    else:print("invalid request")
l1=[10,20,30,40]
l2=[50,60,70,80]
calculator(l1,l2,"multiply")