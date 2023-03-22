# my_tuple = (1, 2, 3)
# my_list = [1, 2, 3]
# my_set = {1, 2, 3}

# def my_custom_filter(numbers):
#     filtered_numbers = []
#     for number in my_list:
#         if number % 5 == 0:
#             filtered_numbers.append(number)
#
#     return filtered_numbers
#
#
# my_list = list(range(100))
# my_list = my_custom_filter(my_list)
#
# print(my_list)


# from random import shuffle
#
#
# # def filter_number(element):
# #     # if element % 5 == 0:
# #     #     return True
# #     #
# #     # return False
# #     return element % 5 == 0  # (element % 5 == 0) => will result in True or False
#
#
# my_list = list(range(100))
# shuffle(my_list)
#
# print('initial list', my_list)
# my_list = list(filter(lambda number: number % 5 == 0, my_list))
# print('filtered_list', my_list)


# my_list = list(range(100))
# [0, 1, 2, 3] ---> map ==> [0, 1, 4, 9]
# [0, 1, 2, 3] ---> map ==> [0, 2, 4, 6]
# [0, 1, 2, 3] ---> map ==> [True, False, True, False]
# mapped_list = []
# for element in my_list:
#     mapped_list.append(element ** 2)
# print('mapped_list', mapped_list)
# my_list = list(map(lambda element: element ** 2, my_list))
# print('my_list', my_list)
# my_list = list(map(lambda element: element * 2, my_list))
# print('my_list', my_list)
# my_list = list(map(lambda element: element % 2 == 0, my_list))
# print('my_list', my_list)
# my_list = list(map(lambda element: element if element % 2 == 0 else "", my_list))
# another_list = list(map(lambda element: element if element % 2 == 0 else "", my_list))
# another_list = list(map(lambda element: element * 2, my_list))
# print('my_list', my_list)
# print('another_list', another_list)
#
# # def map(f, sequence):
# #     for i in sequence:
# #         f(i)
#

# from students import students
#
# # ["B", "A", "E"]
# output_students = list(filter(lambda student: student.get("grade", 0) >= 5, students))
# output_students = sorted(output_students, key=lambda student: student["grade"], reverse=True)
# # [{'name': 'B', 'grade': 9}, {'name': 'A', 'grade': 7}, {'name': 'E', 'grade': 6}]
# # ["B", "A", "E"]
# output_students = list(map(lambda student: student["name"], output_students))
# print('output_students', output_students)

# my_list = list(range(10))
# # my_list = list(filter(lambda n: n % 3 == 0, my_list))
# # print('my_list', my_list)
# my_list = [number for number in my_list if number % 3 == 0]
# print('my_list', my_list)

# my_list = list(range(10))
# # my_list = list(map(lambda n: n ** 2, my_list))
# # print('my_list', my_list)
# my_list = [n ** 2 for n in my_list]
# print('my_list', my_list)

# my_list = list(range(10))
# my_list = list(map(lambda n: n if n % 2 == 0 else "", my_list))
# print('my_list', my_list)
# print('init list', my_list)
# my_list = [(n if n % 2 == 0 else "") for n in my_list]
# print('my_list', my_list)  # [0, "", 2, "", 4, "", ..., 8, ""]
# my_list = [n for n in my_list if n != ""]
# my_list = [n for n in my_list if type(n) == int]
# print('my_list', my_list)
# my_list = [n ** 2 for n in my_list if n % 2 == 0]
# print('my_list', my_list)

# def get_value(n):
#     if n < 5:
#         return n
#
#     if n % 2 == 0:
#         return True
#
#     return "abc"
#
#
# my_list = list(range(10))
# my_list = [get_value(n) for n in my_list]
# print('my_list', my_list)

# def filter_value(n):
#     if n < 5:
#         return True
#
#     # if n % 2 == 0:
#     #     return True
#     #
#     # return False
#     return n % 2 == 0
#
#
# my_list = list(range(10))
# my_list = [n ** 2 for n in my_list if filter_value(n)]
# print('my_list', my_list)

# from students import students
# # ["B", "A", "E"]
#
# # output_students = [
# #     student["name"]
# #     for student in sorted(students, key=lambda student: student.get("grade", 0), reverse=True)
# #     if student.get("grade", 0) >= 5
# # ]
# output_students = [student for student in students if student.get("grade", 0) >= 5]
# output_students = [
#     student["name"]
#     for student in sorted(output_students, key=lambda student: student["grade"], reverse=True)
# ]
# print('output_students', output_students)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print('#1. my_list_length =', len(my_list))

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# output = [n for n in my_list if n % 2 == 0]
# output = list(n for n in my_list if n % 2 == 0)
# output = tuple(n for n in my_list if n % 2 == 0)
# output = set(n for n in my_list if n % 2 == 0)
# output = [n for n in my_list if n % 2 == 0]
# output = {n for n in my_list if n % 2 == 0}
# output = (n for n in my_list if n % 2 == 0)
# print('output', type(output), output)

# animals = ["cat", "dog", "elephant"]
# children = ["Ionut", "Daniel", "Marcel"]
#
# # output = ???
# # [("cat", "Ionut"), ("dog", "Daniel"), ("elephant", "Marcel)]
# output = []
# for index, animal in enumerate(animals):
#     output.append((animal, children[index]))
# print(output)

# animals = ["cat", "dog", "elephant"]
# children = ["Ionut", "Daniel", "Marcel", "Popescu"]
# # [("cat", "Ionut"), ("dog", "Daniel"), ("elephant", "Marcel)]
# output = []
# for index, animal in enumerate(animals):
#     output.append((animal, children[index]))
# print(output)

# animals = ["cat", "dog", "elephant", "fish"]
# children = ["Ionut", "Daniel", "Marcel"]
# # [("cat", "Ionut"), ("dog", "Daniel"), ("elephant", "Marcel)]
# output = []
# for index, animal in enumerate(animals):
#     try:
#         output.append((animal, children[index]))
#     except IndexError:
#         pass
# print(output)

# animals = ["cat", "dog", "elephant", "fish"]
# children = ["Ionut", "Daniel", "Marcel"]
# # output1 = list(zip(animals, children))
# # output2 = list(zip(children, animals))
# # print('output1', output1)
# # print('output2', output2)

# output = list(
#     zip(
#         ["a", "b", "c", "d"],
#         [1, 2],
#         [True, True, False, True],
#         [2.5, True, "abc", (1, 2, 3)]
#     )
# )
# print('output', output)

# from random import shuffle
#
# animals = ["cat", "dog", "elephant", "fish"]
# shuffle(animals)
# print('animals', animals)
# children = ["Ionut", "Daniel", "Marcel"]
# shuffle(children)
# print('children', children)
# output = list(zip(animals, children))
# print('output', output)

# from itertools import zip_longest
#
# clients = ["a", "b", "c", "d"]
# budgets = [100, 50, 300]
#
# output = list(zip_longest(clients, budgets, fillvalue=0))
# print('output', output)  # [('a', 100), ('b', 50), ('c', 300), ('d', 0)]

# keys = ["name", "grade", "city"]
# values = ["Mihai", 5, "Craiova"]
# # output = {"name": "Mihai", "grade": 5, "city": "Craiova"}
# output = dict(zip(keys, values))
# print("output", output)
# # dict([("k1", "v1"), ("k2", "v2", ("k3", "v3"])

# keys = ["name", "grade", "city"]
# students = [
#     ["Mihai", 5, "Craiova"],
#     ["Ionut", 6, "Iasi"],
#     ["Marcel", 2, "Sibiu"]
# ]
# # [
# #   {"name": "Mihai", "grade": 5, "city": "Craiova"},
# #   {"name": "Ionut", "grade": 6, "city": "Iasi"},
# #   {"name": "Marcel", "grade": 2, "city": "Sibiu"},
# # ]
# # output = list(dict(zip(keys)))
# output = [
#     {key: value for key, value in zip(keys, student)}
#     for student in students
# ]
# print('output', output)

keys = ["name", "grade", "city"]
values = ["Mihai", 5, "Craiova"]
# output = {"name": "Mihai", "grade": 5, "city": "Craiova"}
# output = dict(zip(keys, values))
output = {key: value for key, value in zip(keys, values)}
print('output', output)
