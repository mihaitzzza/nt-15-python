# a = "15"
# b = int(a)
# c = 3
#
# print(a, type(a))
#
# # print("Valid instruction.")

# user_input = input("insert a number: ")
# user_input = int(user_input)
# print(user_input, type(user_input))

# user_input = input("insert a number: ")

# try:
#     user_input = int(user_input)
#     print(undefined_variable)
# except ValueError as e:
#     print(e)
#     print(f"You inserted '{user_input}' which is not a valid number!")

# try:
#     user_input = int(user_input)
#     print(undefined_variable)
# except Exception as e:
#     print("I caught the following exception: ", e, type(e))

# try:
#     user_input = int(user_input)
#     print(undefined_variable)
# except (ValueError, NameError) as e:
#     print("I caught the following exception: ", e, type(e))

# try:
#     user_input = int(user_input)
#     print(undefined_variable)
# except ValueError as e:
#     print("I caught a ValueError exception:", e)
# except NameError as e:
#     print("I caught a NameError exception:", e)
# except IndexError as e:
#     print("I caught a IndexError exception:", e)
# except KeyError as e:
#     print("I caught a KeyError exception:", e)

# user_name = input("Name: ")
# print("Name: ", user_name)
#
# user_age = input("Age: ")
# try:
#     print("Age: ", int(user_age))
# except ValueError:
#     print("Age: ", user_age, "(this is invalid value.)")
#
# user_city = input("City: ")
# print("City: ", user_city)

# user_age = input("Age: ")
#
# try:
#     user_age = int(user_age)
# except ValueError:
#     print("Invalid age. Please try again later.")
#
# if (type(user_age) == int) and (user_age >= 18):
# #         True             and       True           => True (example for user_age = "20")
# #         True             and       False           => False (example for user_age = "5")
# #         False            and       ????           => False (example for user_age = <whatever_string_not_an_integer>)
#     print("You are a grown up!")

# user_age = input("Age: ")
#
# try:
#     user_age = int(user_age)
# except ValueError:
#     print("Invalid age. Please try again later.")
#
# else:
#     if user_age >= 18:
#         print("You are a grown up!")
#     else:
#         print("You are a child!")
# finally:
#     print("End of the program!")

# import sys
#
# user_age = input("Age: ")
#
# try:
#     user_age = int(user_age)
# except ValueError:
#     print("Invalid age. Please try again later.")
#     sys.exit(0)
#
# if user_age >= 18:
#     print("You are a grown up!")
# else:
#     print("You are a child!")

# user_age = int(input("Age: "))
# >= 18 -> grown up
# >= 65 -> retired
# < 18 -> child
# < 14 -> without ID

# if user_age >= 18:
#     print("You are a grown up")
#
#     if user_age >= 65:
#         print("You are a retired person")
# else:
#     print("You are a child")
#
#     if user_age < 14:
#         print("You do not have an ID")

# if user_age < 14:
#     print("You do not have an ID")
# elif user_age < 18:
#     print("You are a child")
# elif user_age < 65:
#     print("You are a grown up")
# else:
#     print("You are a retired person")

# if user_age >= 18:
#     print("Grown up!")
# else:
#     print("You are not a grown up!")

# if user_age < 18:
#     print("You are not a grown up!")
# else:
#     print("Grown up!")

# if user_age >= 18:
#     print("Grown up!")

# if user_age < 18:  # not (user_age >= 18)
#     pass
# else:
#     print("Grown up!")

# while True:
#     print("Inside while loop")

# my_numbers = [54, 23, 78, -2]  # len(my_numbers) = 4
# my_numbers = (54, 23, 78, -2)  # len(my_numbers) = 4
# my_numbers = {54, 23, 78, -2}  # len(my_numbers) = 4

my_numbers = [54, 23, 54, 78, -2]

# for item in my_numbers:
#     print(f"Item with value = {item} is on index = {my_numbers.index(item)}")

# # print(list(enumerate(my_numbers)))
# for element in enumerate(my_numbers):
#     # print(element, type(element))
#     print(f"Item with value = {element[1]} is on index = {element[0]}")

# my_tuple = (56, -2, 14)  # print(my_tuple, type(my_tuple))
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)

# for index, number in enumerate(my_numbers):
#     print(f"Item with value = {number} is on index = {index}")

# my_numbers = [12, 56, -2, 14]
# index = 0
#
# while index < len(my_numbers):
#     print(f"Item with value = {my_numbers[index]} is on index = {index}")
#     index = index + 1

# is_valid_age = False
# while not is_valid_age:
#     age = input('Age: ')
#
#     try:
#         age = int(age)
#     except ValueError:
#         print("Invalid valid. Try again.")
#     else:
#         is_valid_age = True
#
#         if age >= 18:
#             print("You are a grown up!")
#         else:
#             print("You are a child!")

# is_valid_age = False
# while not is_valid_age:
#     try:
#         age = int(input('Age: '))
#     except ValueError:
#         print("Invalid valid. Try again.")
#     else:
#         is_valid_age = True
#
#         if age >= 18:
#             print("You are a grown up!")
#         else:
#             print("You are a child!")

# for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     if number % 2 == 0:
#         print(f"Number = {number} is even.")
#         break  # to check what continue does instead of break
#
#     print(f"Number = {number} is odd.")

# for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     pass

# a = input()
#
# if a < 18:
#     pass

while True:
    try:
        age = int(input('Age: '))
    except ValueError:
        print("Invalid valid. Try again.")
        continue

    if age >= 18:
        print("You are a grown up!")
    else:
        print("You are a child!")

    break
