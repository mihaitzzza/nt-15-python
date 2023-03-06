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

def my_function(a, b):
    # for i in range(b):
    #     print(a)
    # print(str(a) * b)
    print(f"{a}\n" * b)


my_function(2, 10)
# my_function(10, 2)
