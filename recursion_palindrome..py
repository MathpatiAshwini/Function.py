def palindrome(v):
    if len(v) < 1:
        return True
    else:
        if v[0] == v[-1]:
            return palindrome(v[1:-1])
        else:
            return False

var = input(("Enter a value: "))
if(palindrome(var)):
    print(var,"The input is a palindrome")
else:
    print(var,"The input is not a palindrome")
