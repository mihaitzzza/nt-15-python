# def get_gcd(a, b):
#     if b == 0:
#         return a
#
#     return get_gcd(b, a % b)
#
#
# assert get_gcd(12, 6) == 6
# assert get_gcd(6, 4) == 2

# def get_gcd(a, b):
#     min_n = min(a, b)
#
#     for i in range(min_n, 1, -1):
#         if a % i == 0 and b % i == 0:
#             return i
#
#     return 1

# def get_gcd(a, b):
#     gcd = min(a, b)
#
#     while a % gcd != 0 or b % gcd != 0:
#         gcd -= 1
#
#     return gcd
#
#
# assert get_gcd(12, 6) == 6
# assert get_gcd(6, 4) == 2

# get_gcd(6, 4)
# ====> 6 % 4 = 2
# get_gcd(4, 2)
# ====> 4 % 2 = 0
# get_gcd(2, 0)


import math


class Fraction:
    def __init__(self, numerator, denominator):
        if type(numerator) != int or type(denominator) != int:
            raise TypeError("Numerator and denominator should be integer!")

        if denominator == 0:
            raise ZeroDivisionError

        gcd = math.gcd(numerator, denominator)

        self.__numerator = numerator // gcd
        self.__denominator = denominator // gcd

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __eq__(self, other):
        if type(other) == int:
            other = Fraction(other, 1)
        elif type(other) != Fraction:
            raise TypeError(f"Cannot compare fraction with {type(other).__name__}")

        return self.__numerator == other.__numerator and self.__denominator == other.__denominator

    def __float__(self):
        return self.__numerator / self.__denominator

    def __add__(self, other):
        if type(other) == int:
            other = Fraction(other, 1)
        elif type(other) != Fraction:
            raise TypeError(f"Cannot add fraction with {type(other).__name__}")

        new_numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if type(other) == int:
            other = Fraction(other, 1)
        elif type(other) != Fraction:
            raise TypeError(f"Cannot sub fraction with {type(other).__name__}")

        new_numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def inverse(self):
        if self.__numerator == 0:
            raise TypeError("We cannot create the inverse of this function because numerator is 0.")

        return Fraction(self.__denominator, self.__numerator)


if __name__ == "__main__":
    # 1/2 => valid | 2/0 => INVALID | "a"/"b" => INVALID | (1, 2, 3)/["a", "b", "c'] => INVALID
    x = Fraction(1, 2)
    assert x._Fraction__numerator == 1
    assert x._Fraction__denominator == 2

    try:
        x = Fraction(2, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False, "Division with 0 is allowed!"

    try:
        x = Fraction("a", "b")
    except TypeError:
        assert True
    else:
        assert False, "Numerator and denominator can be set as non-integer."

    x = Fraction(6, 12)
    assert x._Fraction__numerator == 1
    assert x._Fraction__denominator == 2
    assert str(x) == "1/2"
    assert x.inverse() == Fraction(2, 1)

    x = Fraction(1, 2)
    y = Fraction(3, 4)
    assert x + y == Fraction(5, 4)
    assert x - y == Fraction(-2, 8)

    # r = Fraction(1, 2) + "a"
    # print(r)

    # r = Fraction(1, 2) + 2  # 1/2 + 2/1
    # print(r)

    # assert Fraction(1, 2) == 2
    assert Fraction(8, 4) == 2

    x = Fraction(1, 2)
    assert float(x) == 0.5
