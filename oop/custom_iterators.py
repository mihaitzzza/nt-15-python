# # l = [1, 2, 3, 4, 5]
# # t = (1, 2, 3, 4, 5)
# # s = {1, 2, 3, 4, 5}
# d = {"a": 1, "b": 2, "c": 3}
#
# for element in d.items():
#     print(element)

# l_iterator = iter([1, 2, 3, 4, 5])
#
# print(next(l_iterator))
# print(next(l_iterator))
# print(next(l_iterator))
# print(next(l_iterator))
# print(next(l_iterator))
# print(next(l_iterator))

# # 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# class Fibonacci:
#     def __init__(self, n):
#         self.__previous_value = 0      # 0 => 1 => 1 => 2
#         self.__current_value = 1       # 1 => 1 => 2 => 3
#         self.__n = n  # how many numbers to generate
#         self.__index = 0  # how many numbers we already generated
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__index >= self.__n:
#             raise StopIteration()
#
#         value = self.__current_value
#
#         aux = self.__previous_value
#         self.__previous_value = self.__current_value
#         self.__current_value = self.__current_value + aux
#         self.__index += 1
#
#         return


from abc import ABC, abstractmethod


class Fibonacci(ABC):
    def __init__(self):
        self._previous_value = 0  # 0 => 1 => 1 => 2
        self._current_value = 1  # 1 => 1 => 2 => 3

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        value = self._current_value

        aux = self._previous_value
        self._previous_value = self._current_value
        self._current_value = self._current_value + aux

        return value


class FibonacciMaxNumbers(Fibonacci):
    def __init__(self, n):
        super().__init__()

        self.__n = n  # how many numbers to generate
        self.__index = 0  # how many numbers we already generated

    def __next__(self):
        if self.__index >= self.__n:
            raise StopIteration()

        self.__index += 1

        return super().__next__()


class FibonacciMaxValue(Fibonacci):
    def __init__(self, max_value):
        super().__init__()

        self.__max_value = max_value  # generated numbers until this value

    def __next__(self):
        if self._current_value > self.__max_value:
            raise StopIteration()

        return super().__next__()


class FibonacciBetween(Fibonacci):
    def __init__(self, min_value, max_value):
        # if min_value > max_value:
        #     raise ValueError("This insane!!!")

        super().__init__()

        self.__min_value = min(min_value, max_value)
        self.__max_value = max(min_value, max_value)

    def __next__(self):
        while True:
            value = super().__next__()

            if value >= self.__max_value:
                raise StopIteration()

            if value >= self.__min_value:
                return value


# my_custom_iterable = Fibonacci(10)
# fibonacci_iterator = iter(my_custom_iterable)

# # my_custom_iterable = FibonacciMaxValue(12530)
# my_custom_iterable = FibonacciMaxNumbers(10)
# fibonacci_iterator = iter(my_custom_iterable)
# my_custom_iterable = Fibonacci()
# fibonacci_iterator = iter(my_custom_iterable)

# print(next(fibonacci_iterator))
# print(next(fibonacci_iterator))
# print(next(fibonacci_iterator))

# assert next(fibonacci_iterator) == 1
# assert next(fibonacci_iterator) == 1
# assert next(fibonacci_iterator) == 2
# assert next(fibonacci_iterator) == 3
# assert next(fibonacci_iterator) == 5

# for i in fibonacci_iterator:
#     if i > 100000:
#         break
#     print(i)

# for index, i in enumerate(fibonacci_iterator):
#     if index > 1000:
#         break
#     print(i)

my_fibonacci = FibonacciBetween(25, 12)
fibonacci_iterator = iter(my_fibonacci)

for i in fibonacci_iterator:
    print(i)
