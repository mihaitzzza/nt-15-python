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


from random import shuffle


# def filter_number(element):
#     # if element % 5 == 0:
#     #     return True
#     #
#     # return False
#     return element % 5 == 0  # (element % 5 == 0) => will result in True or False


my_list = list(range(100))
shuffle(my_list)

print('initial list', my_list)
my_list = list(filter(lambda number: number % 5 == 0, my_list))
print('filtered_list', my_list)

