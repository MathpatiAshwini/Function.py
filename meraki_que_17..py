def calculator(number_x,number_y,operation):
    if(operation=="add"):
        print(number_x+number_y)
    elif(operation=="sub"):
        print(number_x-number_y)
    elif(operation=="divide"):
        print(number_x/number_y)
    elif(operation=="multiply"):
        print(number_x*number_y)
    else:
        print("invalid request")
calculator(14,2,"add")
calculator(14,2,'sub')
calculator(14,2,"divide")
calculator(14,2,"multiply")