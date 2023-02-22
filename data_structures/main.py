# my_list = []  # my_list = list()
#
# print(my_list, type(my_list))

# # my_numbers = [2, 4, -3, 12, 10, -15]
# # #             0  1  2    3   4   5
# my_numbers = ['a', 'b', 'c', 'd', 'e', 'f']
# #              0    1    2    3    4    5
# #             -6    -5   -4   -3   -2   -1
# # print(my_numbers[1])
# # print(my_numbers[100])  # IndexError
# # print(my_numbers[-3])
# print("length of the list =", len(my_numbers))
# print(my_numbers[2], my_numbers[-4])

# my_numbers = ['a', 'b', 'c', 'd', 'e', 'f']
# #              0    1    2    3    4    5
# #             -6    -5   -4   -3   -2   -1
# # slice: my_numbers[start:end:step]
# my_slice = my_numbers[::]  # shallow copy of `my_numbers` list
# print('my_numbers', my_numbers, type(my_numbers))
# print('my_slice', my_slice, type(my_slice))

# my_numbers = ['a', 'b', 'c', 'd', 'e', 'f']
# #              0    1    2    3    4    5
# #             -6    -5   -4   -3   -2   -1
# # my_slice = my_numbers[1:4:1]  # my_numbers[start:end:step]
# # my_slice = my_numbers[1:4:2]  # my_numbers[start:end:step]
# # my_slice = my_numbers[4:2:-1]  # my_numbers[start:end:step]
# # my_slice = my_numbers[::-1]  # get `my_numbers` in reversed order
# # my_slice = my_numbers[1:4]
# # my_slice = my_numbers[::]  # is the same with my_numbers[0:len(my_numbers):1]
# my_slice = my_numbers[1:]
# print('my_numbers', my_numbers, type(my_numbers))
# print('my_slice', my_slice, type(my_slice))

# my_numbers = ['a', 'b', 'c', 'd', 'e', 'f']
# print(my_numbers)
# my_numbers.append('g')
# print(my_numbers)
# my_numbers.insert(1, 'h')
# print(my_numbers)

# my_string = "Ana are mere"
# # print(my_string[::-1])
# my_list = list(my_string)
# print(my_list, type(my_list))

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b, a is b, a is not b)
# a.append(4)
# print(a, b, a == b, a is b)

# a = [1, 2, 3]
# b = a
# print(a == b, a is b)
# a.append(4)
# print(a == b, a is b)
# print(a)
# print(b)
# b.append(5)
# print(a == b, a is b)
# print(a)
# print(b)
# b = [1, 2, 3, 4, 5, 6]
# print(a == b, a is b)

# my_string = "mere pere struguri"  # ["mere", "pere", "struguri"]
# my_list = my_string.split(" ")
# print(my_list, type(my_list))
# # my_string = ";".join(my_list)
# my_string = " ".join(my_list)
# print('my_string', my_string)

# my_tuple = ()  # my_tuple = tuple()
# my_tuple = (1, 2, 3, True, 'a')
# print('my_tuple', my_tuple, type(my_tuple))
# print(my_tuple[-2])
# print(my_tuple[1:])

# my_tuple = (1, 2, 3)
# print('my_tuple', my_tuple)
# my_list = list(my_tuple)
# print('========================> ', my_tuple is my_list)
# print(my_list, type(my_list))
# my_list.append(4)
# my_tuple = tuple(my_list)
# print('my_tuple', my_tuple)

# my_tuple = (1, 2, 3)
# my_tuple = (1, 2, 3, 4)

# a = (1, 2, 3)
# c = a
# # print(c is a)  # True
# a = (1, 2, 3, 4)
# print('c', c)

# my_list = [1, 2, 3]
# my_list_2 = my_list
# my_tuple = ('a', my_list, 'b')
# print('my_tuple', my_tuple, type(my_tuple))
# # my_list.append(4)
# # my_list = [1, 2, 3, 4]
# my_list_2.append(5)
# print('my_tuple', my_tuple, type(my_tuple))
# print('my_list', my_list)

# a = [1]
# b = a
# c = a
# d = a
# e = a
# c.append(2)
# e.append(3)
# print(a, b, c, d, e)
# print(id(a) == id(b), id(b) == id(e))

# my_dict = {}  # my_dict = dict()
# print('my_dict', my_dict, type(my_dict))

# my_dict = {
#     "name": "Mihai",
#     "age": 30
# }
# print(my_dict, type(my_dict))

# my_dict = {
#     "name": "Mihai",
#     "age": 30,
#     2: [1, 2, 3],
#     3: 100,
#     3: "abc",
#     4: "abc",
#     (1, 2, "a"): {"a": 1, "b": [1, 2, 3]},
# }
# print(my_dict, type(my_dict))

# my_dict = {
#     "name": "Mihai",
#     "age": 30,
#     "city": "Craiova",
#     "height": 200,
# }
# print(my_dict, type(my_dict))
# print(my_dict["age"])
# print(my_dict["city"])
# print(my_dict["asdhasiudisadhasidhai"])  # KeyError

# my_dict["age"] = 31
# print(my_dict["age"])
# print(my_dict)
# my_dict["country"] = "Romania"
# print(my_dict)
# del my_dict["height"]
# print(my_dict)

# student_1 = {"name": "Mihai"}
# student_2 = {"name": "Ionel"}
# student_3 = {"name": "Gigel"}
#
# students = [student_1, student_2, student_3]
# print(students)
#
# student_2["promoted"] = True
#
# print(students)


# my_dict = {
#     "name": "Mihai",
#     "age": 30,
#     "city": "Craiova",
#     "height": 200,
# }
# print(list(my_dict.keys()))
# print(list(my_dict.values()))
# print(list(my_dict.items()))

# print("are" in "Ana are mere")
# print(10 in [1, 10, 100])
# print(10 in (1, 10, 100))
# print("name" in {"name": "Mihai", "age": 30})
# # print("Mihai" in {"name": "Mihai", "age": 30}) # this will be False because "Mihai" is not a key in the dict.
# print("Mihai" in {"name": "Mihai", "age": 30}.values())

# my_dict = {
#     "name": "Mihai",
#     "age": 30,
#     "city": "Craiova",
#     "height": 200,
# }
# # print(my_dict["country"])  # KeyError: 'country'
# print(my_dict.get("country"))  # print(my_dict.get("country", None))

# my_set = {}  # !!! This is not a set! It's an empty dictionary.
# my_set = set()
# my_set = {1, None, True, True, True, False, 0, "abc", "aaa"}
# print(my_set, type(my_set))
# print(True in my_set)
# print(0 in my_set)
# print(hash(1))
# print(hash(True))
# print(hash(False))
# print(hash(0))

# my_set = {1, 2, 3}
# my_set.add(4)
# print('my_set', my_set)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# my_list.pop()
# my_list.pop()
# my_list.pop()
# print(my_list)

# my_set = {4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 1, 2, 3, 19, 20}
# print(my_set)
# my_set.pop()
# print(my_set)
# my_set.pop()
# print(my_set)
# my_set.pop()
# print(my_set)
# print(len(my_set))

# my_set_1 = {1, 2, 3}
# my_set_2 = {2, 3, 4}
# print(my_set_1.union(my_set_2))
# print(my_set_1.intersection(my_set_2))
