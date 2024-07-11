immutable_var = (1, 1.0, True, "Urban", [1,2])
print(immutable_var)

mutable_list = [1, 1.0, True, "Urban", [1, 2]]
mutable_list[0] = 2
mutable_list[1] = 2.0
mutable_list[2] = False
mutable_list[3] = "python manage.py startapp"
mutable_list[4] = [3, 4]
print(mutable_list)
