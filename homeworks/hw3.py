# def f():
#     return 5, 3, 2
#
# # result = f()
# # print(result[0])
# # print(result[1])
# # print(result[2])
# a, b, c = f()
# print(a)
# print(b)
# print(c)

# # Exercise Nr. 1 - Sum of all numbers
# def get_sum_from_parameters(*args, **kwargs):
#     total = 0
#
#     for arg in args:
#         # if type(arg) == int or type(arg) == float:
#         #     total += arg
#         # try:
#         #     total += float(arg)
#         # except ValueError:
#         #     pass
#         if isinstance(arg, (int, float)):
#             total += arg
#
#     # TODO #1: Account for `kwargs` and sum all the numbers in there
#     # TODO #2: Account for every number at any level in both `args` and `kwargs`
#
#     return total
#
#
# print(get_sum_from_parameters(1, 5, -3, "abc", "12", [12, 56, "cad"]))
# print(get_sum_from_parameters(1, 5, -3, "abc", "12", [12, 56, [1, 2], "cad"]))
# print(get_sum_from_parameters(1, 5, -3, "abc", "12", [12, 56, [1, 2, {3, 4}], "cad"]))
# print(get_sum_from_parameters())
# print(get_sum_from_parameters(2, 4, "abc", param_1=2))
# print(get_sum_from_parameters(2, 4, "abc", param_1=2, param_2="abc"))
# print(get_sum_from_parameters(2, 4, "abc", param_1=2, param_2="abc", param_3=2.5))


# # Exercise Nr. 2 - Recursive sum with "multiple return values"
# def get_rec_sum(n: int) -> tuple:
#     if n == 0:
#         return 0, 0, 0
#
#     total_sum, even_sum, odd_sum = get_rec_sum(n - 1)
#
#     total_sum += n
#     if n % 2 == 0:
#         even_sum += n
#     else:
#         odd_sum += n
#
#     return total_sum, even_sum, odd_sum
#
#
# total_sum, even_sum, odd_sum = get_rec_sum(5)
# print("total_sum", total_sum)
# print("even_sum", even_sum)
# print("odd_sum", odd_sum)

# Exercise Nr. 3 - Parse input function
def get_integer_from_input():
    user_input = input("Input: ")

    try:
        return int(user_input)
    except ValueError:
        return 0


print(get_integer_from_input())
