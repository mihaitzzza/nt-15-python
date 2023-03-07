# def my_first_function():
#     print("Hello from my first function!")
#     print("sum of 5 + 7", 5 + 7)
#     print("End of my function! Good bye")
#
#
# print('-- BEFORE FUNCTION CALL')
# my_first_function()
# print('-- AFTER FUNCTION CALL')
# my_first_function()
# my_first_function()
# my_first_function()
# my_first_function()
# my_first_function()
# my_first_function()
# my_first_function()
# my_first_function()
# my_first_function()


# def show_sum_of_numbers():
#     while True:
#         try:
#             a = int(input("a = "))
#             break
#         except ValueError:
#             print("Value for a is not a number. Please try again.")
#
#     while True:
#         try:
#             b = int(input("b = "))
#             break
#         except ValueError:
#             print("Value for b is not a number. Please try again.")
#
#     print(f"Sum of {a} and {b} is {a + b}")


# show_sum_of_numbers()
# show_sum_of_numbers()
# show_sum_of_numbers()


# def read_number():
#     number = input('number: ')
#     print('number', number)

# def get_number():
#     number = int(input('number: '))
#     return number
#
#
# def show_sum_of_numbers():
#     a = get_number()
#     b = get_number()
#     print("First number is: ", a)
#     print("Second number is: ", b)
#     print("Sum = ", a + b)
#
#
# show_sum_of_numbers()
# show_sum_of_numbers()
# show_sum_of_numbers()


# def get_number():
#     number = input("number: ")
#     return int(number)
#
#
# def get_validated_number():
#     while True:
#         try:
#             number = get_number()
#             return number
#         except ValueError:
#             print("Value for input is not a number. Please try again.")
#
#
# def show_sum_of_numbers(a, b):
#     print(f"Sum of {a} and {b} is {a + b}")
#
#
# # show_sum_of_numbers(2, 9)
# # show_sum_of_numbers(7, 5)
# # show_sum_of_numbers(5, 7)
# # a = get_validated_number()
# # b = get_validated_number()
# # show_sum_of_numbers(b, a)
# n1 = get_validated_number()
# n2 = get_validated_number()
# show_sum_of_numbers(n1, n2)


# def my_function(my_list):
#     my_list.append(4)
#
#
# l1 = [1, 2, 3]
#
# print("1.", l1)
#
# my_function(l1)
#
# print("2.", l1)
#
# my_function(l1)
#
# print("3.", l1)

# def my_function(my_list):
#     my_list.append(4)
#     return my_list
#
#
# l1 = [1, 2, 3]
# l2 = my_function(l1)
#
# l1.append("x")
# l2.append("y")
#
# print("1.", l1)  # 1, 2, 3, 4
# print("2.", l2)  # 1, 2, 3, 4
# print("3.", l1 == l2)  # True
# print("4.", l1 is l2)  # True


# def my_function(my_list):
#     my_list = my_list.copy()
#
#     my_list.append(4)
#     return my_list
#
#
# l1 = [1, 2, 3]  # [1, 2, 3]
# l2 = my_function(l1)  # [1, 2, 3, 4]
#
# assert l1 is not l2
# assert l1 != l2

# def my_function(my_list):
#     my_list = list(my_list)  # my_list.copy(); my_list[:]
#     my_list.append(4)
#     return my_list
#
#
# l1 = [1, 2, 3]  # [1, 2, 3]
# l2 = my_function(l1)  # [1, 2, 3, 4]
#
# assert l1 is not l2
# assert l1 != l2


# def sort(my_list):
#     pass


# numbers = [1, 6, 2, 8, 3]
# # sort(numbers)
# # r = numbers.sort()
# r = sorted(numbers)
# print('r', r)


# def my_function(a, b):
#     print(a + b)


# my_function(2, 7)  # 9
# my_function("a", "c")  # "ac"
# my_function("a", 7)  # ERROR!
# my_function([1, 2, 3], [3, 4])  # [1, 2, 3, 3, 4]

# def my_function(a, b):
#     # for i in range(b):
#     #     print(a)
#     # print(str(a) * b)
#     print(f"{a}\n" * b)
#
#
# my_function(2, 10)
# # my_function(10, 2)

# def f(param_1="abc"):
#     print(param_1)
#
#
# f()
# f(param_1="def")

# def f(param_1, param_2, param_3="abc"):
#     print(param_1, param_2, param_3)
#
#
# f("a", "b")
# f("a", "b", param_3="def")

# def do_math(a, b, operation="+"):
#     if operation == "*":
#         return a * b
#
#     if operation == "/":
#         return a / b
#
#     if operation == "-":
#         return a - b
#
#     return a + b
#
#
# print(do_math(2, 7))
# print(do_math(2, 7, operation="*"))

# def f(a, b, c, *args, param1="abc"):  # variable-length-arguments
#     print(a, b, c, args, param1)
#
#
# # f()
# # f(10, -5)
# # f(7)
# f(7, 1, 2)
# f(7, 10, 2, 7, 8, 2, param1="def")
# f(7, 10, 2, 7, 8, 2, 0, 0, 1, 2, 5, param1="efg")
# f(7, 10, 1, 2, 5)


# def f(*args, **kwargs):  # variable-length arguments (args) & keyword-variable-length arguments (kwargs)
#     # print(args, kwargs)
#     pass
#
#
# f()
# f(1, 2, 3)
# f(1, 2, 3, 4, 5)
# f(1, 2, 3, 4, 5, p1=2, p2="abc")
# f(1, 2, 3, 4, 5, p1=2, p2="abc", p3=[12, 3])
# f(1, 2, "a", 4, 5, p1=2, p2="abc", p3=[12, 3])

# def f1():
#     pass
#
#
# def f2(a):
#     pass
#
#
# def f3(a, k1=None):
#     pass
#
# def f4(*args):
#     pass
#
# def f4(**kwargs):
#     pass
#
#
# def f(a, b, *args, k1=None, k2=None, k3=None, **kwargs):
#     pass


# def f(a, b):
#     return a + b


# a = f
# print(a(2, 7))  # f(2, 7)

# def g(my_function):
#     return my_function(2, 7)
#
#
# print(g(f))

# def g():
#     def f(a, b):
#         return a + b
#
#     return f
#
#
# a = g()
# print(a(2, 7))


# def f():
#     def g():
#         my_variable = 30
#         print("my_variable value inside g", my_variable)
#
#     my_variable = 20
#     g()
#     print("my_variable value inside f", my_variable)
#
#
# my_variable = 10
#
# f()
# print("my_variable value in main program", my_variable)


# def f():
#     def int(x):
#         return "ha, ha"
#
#     a = int("10")
#     print("f1", a)
#
#
# a = int("12")
# print("main", a)
#
# f()


# Print all numbers from 0 to n
# def f(n):
#     if n > 0:
#         f(n - 1)
#
#     print(n)

# def f(n):
#     if n == 0:
#         return [0]
#
#     previous_step_list = f(n-1)
#     previous_step_list.append(n)
#
#     return previous_step_list
#
#
# l = f(5)  # 0, 1, 2, 3, 4, 5
# print("function result", l)
# l = f(7)  # 0, 1, 2, 3, 4, 5, 6, 7
# print("function result", l)

# def f(a: int, b: int):
#     print(a + b)
#
#
# f(2, 5)
# f("abc", "def")
# f([1, 2, 3], [3, 4])
# # f(2, "abc")
# # f(None, None)


# def f(n: int) -> list:
#     if n % 2 == 0:
#         return list(reversed(range(n)))
#
#     return list(range(n))
#
#
# my_var = f(5)  # [0, 1, 2, 3, 4]
# print('my_var', my_var)
#
# my_var = f(4)
# print('my_var', my_var)

def f(a: str) -> None:
    print(a.split(" "))


# f("a b c")

