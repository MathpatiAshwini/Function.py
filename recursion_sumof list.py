#  Write a Python program of recursion list sum. Go to the editor
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21

def sum(list):
	total = 0
	for i in list:
		if type(i) == type([]):
			total = total + sum(i)
		else:
			total = total + i

	return total
print( sum([1, 2, [3,4],[5,9]]))
