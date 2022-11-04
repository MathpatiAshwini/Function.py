# def add_numbers_print(number_x, number_y):
#     number_sum = number_x + number_y
#     print (number_sum)
# sum4 = add_numbers_print(4,5)
# print(sum4)
# print(type(sum4))


def menu(day):
    if day == "monday":
        return"Butter Chicken"
    elif day == "tuesday":
        return"Mutton Chaap"
    else:
       return"Chole Bhature"
mon_menu = menu("monday")
print(mon_menu)
tues_menu = menu("tuesday")
print(tues_menu)
fri_menu = menu("friday")
print(fri_menu)