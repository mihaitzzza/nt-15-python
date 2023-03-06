numbers = [1, 6, 2, 8, 3]

# numbers.sort()
# print('numbers', numbers)

# # Solution #1
# ordered_numbers = numbers.copy()
# print(numbers)
# print(ordered_numbers)
# print(numbers is ordered_numbers)
# ordered_numbers.sort()
# print("asc", ordered_numbers)
# ordered_numbers.sort(reverse=True)  # ordered_numbers.reverse()
# print("desc", ordered_numbers)
# print("initial list", numbers)

# # Solution #2
# ordered_numbers = sorted(numbers)
# print("asc", ordered_numbers)
# # ordered_numbers.sort(reverse=True)  # ordered_numbers.reverse()
# ordered_numbers = sorted(numbers, reverse=True)
# print("desc", ordered_numbers)
# print("initial list", numbers)

# Solution #3
ordered_numbers = numbers[:]
ordered_numbers.sort()
print("asc", ordered_numbers)
ordered_numbers = ordered_numbers[::-1]
print("desc", ordered_numbers)
print("initial list", numbers)
