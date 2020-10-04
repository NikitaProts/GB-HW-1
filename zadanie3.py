def my_func(var_1, var_2, var_3):
    var_list = []
    var_list.extend([var_1, var_2, var_3])
    var_list.pop(var_list.index(min(var_list)))
    print(sum(var_list))

# my_func(1,2,3)
