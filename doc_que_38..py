
# a=[(-12, 2, -6)  
# (-12, 2, -5)  
# (45, 1, 6)    
# (45, 5, 15)   
# (4, 1, 4)     
# (15, -5, 3)] 

def is_divide_by(number, a, b):
    return not(number%a or number%b)

print(is_divide_by(-12,2,-6))
print(is_divide_by(-12, 2, -5) ) 
print(is_divide_by(45, 1, 6))   
print(is_divide_by(45, 5, 15)) 
print(is_divide_by(4, 1, 4))     
print(is_divide_by(15, -5, 3))
