# Write a Python program to calculate the value of 'a' to the power 'b'. Go to the editor
# Test Data :
# (power(3,4) -> 81


def power(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)
a=int(input('enter the number'))
b=int(input('enter the number'))
print(power(a,b))

