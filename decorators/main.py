# import random
# import time
#
#
# if __name__ == "__main__":
#     print("I'll wait for 5 seconds...")
#     time.sleep(5)
#     print("I'll continue program execution.")
#
#     my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     print(random.choice(my_numbers))
import time
# def while_loop():
#     max_tries = 3
#     current_try = 1
#     while current_try <= max_tries:
#         user_age = input("Age: ")
#
#         try:
#             user_age = int(user_age)
#         except ValueError:
#             print("Invalid age. Please try again.")
#             current_try += 1
#             continue
#
#         if user_age <= 18:
#             print("You do not have access here.")
#         else:
#             print("Congrats! Access granted.")
#
#         break
#     else:
#         print("You exceeded the number of tries.")
#
#
# def for_loop():
#     max_tries = 3
#     for _ in range(max_tries):
#         user_age = input("Age: ")
#
#         try:
#             user_age = int(user_age)
#         except ValueError:
#             print("Invalid age. Please try again.")
#             continue
#
#         if user_age <= 18:
#             print("You do not have access here.")
#         else:
#             print("Congrats! Access granted.")
#
#         break
#     else:
#         print("You exceeded the number of tries.")


from time import monotonic_ns, sleep

# def iterate_with_while(numbers):
#     start_time = monotonic_ns()
#
#     print("Iterate using 'while' loop.")
#     index = 0
#     while index < len(numbers):
#         # print(numbers[index])
#         index += 1
#
#     end_time = monotonic_ns()
#     execution_time = end_time - start_time
#     execution_time_ms = execution_time / 1000000
#     # print(f"Execution time: {execution_time}(ns)")
#     print(f"Execution time: {execution_time_ms}(ms)")
#
#
# def iterate_with_for(numbers):
#     start_time = monotonic_ns()
#
#     print("Iterate using 'for' loop.")
#     for number in numbers:
#         # print(number)
#         pass
#
#     end_time = monotonic_ns()
#     execution_time = end_time - start_time
#     execution_time_ms = execution_time / 1000000
#     # print(f"Execution time: {execution_time}(ns)")
#     print(f"Execution time: {execution_time_ms}(ms)")


# def execution_time():
#     def a():
#         pass
#
#     return a

# def execution_time(function_to_decorate):
#     def wrapper(*args):
#         start_time = monotonic_ns()
#
#         function_to_decorate(args)
#
#         end_time = monotonic_ns()
#         execution_time = end_time - start_time
#         execution_time_ms = execution_time / 1000000
#         print(f"Execution time: {execution_time_ms}(ms)")
#
#     return wrapper
#
#
# def iterate_with_while(numbers):
#     print("Iterate using 'while' loop.")
#     index = 0
#     while index < len(numbers):
#         index += 1
#
#
# def iterate_with_for(numbers):
#     print("Iterate using 'for' loop.")
#     for number in numbers:
#         pass
#
#
# def s(a, b):
#     return a + b
#
#
# if __name__ == '__main__':
#     # numbers = list(range(100000000))
#     # iterate_with_while(numbers)
#     # iterate_with_for(numbers)
#
#     # numbers = list(range(100000000))
#     # decorated_iterate_with_while = execution_time(iterate_with_while)
#     # decorated_iterate_with_while(numbers)
#     #
#     # decorated_iterate_with_for = execution_time(iterate_with_for)
#     # decorated_iterate_with_for(numbers)
#
#     decorated_s = execution_time(s)
#     my_sum = decorated_s(2, 7)
#     print("my_sum", my_sum)


# def f2(a, b):
#     return a + b

# def f2(*args):
#     print("args inside f2 - this is used for the sum:", args)
#     return sum(args)
#
#
# def f1(*args):
#     # return f2(args)
#     print("args inside f1", args)
#     # args = (1, 2, 7, 8, 10, 11, 11, 11, 11, 22, 33)
#     # f2(args)  # a = args; b = !?!?! ==> TypeError - missing value for b
#     # r = f2(args)  # f2((1, 2, 7, 8, ...))
#     r = f2(*args)  # f2(1, 2, 7, 8, 10, 11, 11, 11, 11, 22, 33)
#     print("r", r)
#
#
# f1(1, 2, 7, 8, 10, 11, 11, 11, 11, 22, 33)

# def execution_time(function_to_decorate):
#     def wrapper(*args):
#         start_time = monotonic_ns()
#
#         result = function_to_decorate(*args)
#
#         end_time = monotonic_ns()
#         execution_time = end_time - start_time
#         execution_time_ms = execution_time / 1000000
#         print(f"Execution time: {execution_time_ms}(ms)")
#
#         return result
#
#     return wrapper
#
#
# def iterate_with_while(numbers):
#     print("Iterate using 'while' loop.")
#     index = 0
#     while index < len(numbers):
#         index += 1
#
#
# def iterate_with_for(numbers):
#     print("Iterate using 'for' loop.")
#     for number in numbers:
#         pass
#
#
# def s(a, b):
#     return a + b
#
#
# if __name__ == '__main__':
#     # numbers = list(range(100000000))
#     # iterate_with_while(numbers)
#     # iterate_with_for(numbers)
#
#     # numbers = list(range(100000000))
#     numbers = list(range(100))
#     decorated_iterate_with_while = execution_time(iterate_with_while)
#     decorated_iterate_with_while(numbers)
#
#     decorated_iterate_with_for = execution_time(iterate_with_for)
#     decorated_iterate_with_for(numbers)
#
#     decorated_s = execution_time(s)
#     my_sum = decorated_s(2, 7)
#     print("my_sum", my_sum)

# from functools import wraps


# def dec(f):
#     @wraps(f)
#     def wrapper(*args, **kwargs):
#         print(f"Before {f.__name__} call")
#         # result = f(*args, kwargs)  # { "kw1": "abc" } => f(..., { "kw1": "abc" })
#         result = f(*args, **kwargs)  # { "kw1": "abc" } => f(..., kw1="abc")
#         print(f"After {f.__name__} call")
#         return result
#
#     return wrapper
#
#
# @dec
# def f1():
#     """This is my awesome f1 function!"""
#     print("--- inside f1")
#
#
# @dec
# def f2(p1):
#     """This is my awesome f2 function!
#     :param p1: Random parameter, I have no idea!
#     """
#     print("--- inside f2", p1)
#
#
# def f3(p1, p2, kw1=None):
#     """This is my awesome f3 function!
#     :param p1: Random parameter, I have no idea!
#     :param p2: Random parameter, I have no idea!
#     :param kw1: Random keyword parameter, I have no idea!
#     """
#     print("--- inside f3", p1, p2, kw1)
#
#
# def f4(kw1=None, kw2=None):
#     """This is my awesome f3 function!
#     :param kw1: Random keyword parameter, I have no idea!
#     :param kw2: Random keyword parameter, I have no idea!
#     """
#     print("--- inside f4", kw1, kw2)
#
#
# if __name__ == '__main__':
#     # print(f2.__name__)
#     # print(f2.__doc__)
#
#     # decorated_f1 = dec(f1)
#     # decorated_f1()
#     # print("\n")
#     #
#     # decorated_f2 = dec(f2)
#     # decorated_f2(10)
#     # print("\n")
#     #
#     # decorated_f3 = dec(f3)
#     # decorated_f3(10, "abc", kw1="def")
#     # print("\n")
#     #
#     # decorated_f4 = dec(f4)
#     # decorated_f4(kw1="def", kw2=[1, 2, 3])
#     # f1()
#     # print('\n')
#     # f2(10)
#
#     # f3(10, 20)
#     #
#     # decorated_f3 = dec(f3)
#     # decorated_f3(10, "abc", kw1="def")
#
#     # print(f3.__name__)
#     # print(f3.__doc__)
#
#     print(f2.__name__)
#     print(f2.__doc__)
#     f2.__wrapped__(10)  # this is possible because of the @wraps decorator from `functools`.


# def dec(f):
#     def wrapper(*args, **kwargs):
#         print('before function call')
#         r = f(*args, **kwargs)
#         print('after function call')
#         return r
#
#     return wrapper

def dec_with_parameter(p1):
    def dec(f):
        def wrapper(*args, **kwargs):
            print("DEC_WITH_PARAMETER: ", p1)
            print('before function call')
            r = f(*args, **kwargs)
            print('after function call')
            return r

        return wrapper

    return dec


@dec_with_parameter(15)
def f1():
    print("--- inside f1")


if __name__ == '__main__':
    f1()
