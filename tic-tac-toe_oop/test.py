# def f(a_list):
#     print("before append:", id(a_list))
#     a_list.append(4)
#     print("after append:", id(a_list))
#
#
# my_list = [1, 2, 3]
# print("id my_list", id(my_list))
#
# f(my_list)
#
# print(my_list)


# def f(a_list):
#     print("id(a_list) [before assignation]", id(a_list))
#     a_list = [1, 2, 3, 4]
#     print("id(a_list) [after assignation]", id(a_list))
#
#
# my_list = [1, 2, 3]
# print("id(my_list)", id(my_list))
#
# f(my_list)
# print(my_list)


def f(a_list):
    a_list.append(4)
    my_list = [1, 2, 3, 4, 5]
    a_list.append(6)


my_list = [1, 2, 3]

f(my_list)

print(my_list)
