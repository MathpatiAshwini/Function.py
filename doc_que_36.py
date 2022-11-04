def swap_values(args):
    temp = args[0]
    args[0] = args[1]
    args[1] = temp
    return args
X=swap_values([9,8])
print(X)

# def swap_values(args): 
#     args[0], args[1] = args[1], args[0]
#     return args
# a=swap_values([3,2])
# print(a)