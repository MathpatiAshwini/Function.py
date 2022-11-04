def calculater():
    while True:
        print("1  addition")
        print("2  substraction")
        print("3  multiplication")
        print("4  division")

        choice=input("enter the your choice:--")

        num1=float(input("enter the frist number:-"))
        num2=float(input("enter the second number:-"))

        if choice=="1":
            print(num1,"+",num2,"=",num1+num2)
        elif choice=="2":
            print(num1,"-",num2,"=",num1-num2)
        elif choice=="3":
            print(num1,"*",num2,"=",num1*num2)
        elif choice=="4":
            if num2==0.0:
                print("divided by error")
            else:
                print(num1,"/",num2,"=",num1/num2)
        else:
            print("invalid error")
calculater()


