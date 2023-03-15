# import my_functions  # N.1.
# from my_functions import my_sum  # N.2
# import my_functions as f  # N.3
# from my_functions import my_sum as s  # N.4


# result = my_functions.my_sum(2, 7)  # N.1
# result = my_sum(2, 7)  # N.2
# result = f.my_sum(2, 7)  # N.3
# result = s(2, 7)  # N.4
# print('result', result)

# from my_functions import my_sum, min_from_list
#
# s = my_sum(2, 7)
# print(s)
#
# m = min_from_list([2, 1, 5])
# print(m)

# from my_functions.integers import my_sum
# from my_functions.lists import min_from_list
#
# s = my_sum(2, 7)
# print(s)
#
# m = min_from_list([2, 1, 5])
# print(m)

# from my_functions.integers import my_sum
# from my_functions.lists import min_from_list
from my_functions import my_sum, min_from_list


def main():
    s = my_sum(2, 7)
    print("sum:", s)

    m = min_from_list([6, 3, -2, 1])
    print("min:", m)


# if __name__ == "__main__":
#     main()

if __name__ == '__main__':
    main()
