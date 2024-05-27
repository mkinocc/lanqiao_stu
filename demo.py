def fun1(my_dict):
    first_value = 0
    for key in my_dict:
        first_value = my_dict[key]
        break
    return first_value

d = {'a':2, 'b':3}
print(fun1(d))
print(fun1(d))