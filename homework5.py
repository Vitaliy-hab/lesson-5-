immutable_var = (1, True, 34, 'early', 'home', [1,3,5,6])
mutable_list = [1, 'home', 45, 567, True]
print(immutable_var, type(immutable_var))
immutable_var = 9
mutable_list[4] = False
print(immutable_var, type(immutable_var))
print(mutable_list, type(mutable_list))
