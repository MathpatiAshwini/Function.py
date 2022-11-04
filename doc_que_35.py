# 35. Kids drink toddy.
# 	Teens drink coke.
# 	Young adults drink beer.
# 	Adults drink whisky.
# 	Make a function that receive age, and return what they drink.
# Rules:-
# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)

def age_drink():
    a=int(input("enter the age "))
    if a>0 and a<=14:
        print("drink toddy")
    elif a>14 and a<=18:
        print("drink coke")
    elif a>18 and a<=21:
        print("drink beer")
    else:
        print( "drink whisky")
age_drink()
