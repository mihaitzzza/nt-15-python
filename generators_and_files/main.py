# # # # print("Hello, World!")
# # # # # print "Hello, World with Python 2.7!"
# # #
# # # # def get_numbers():
# # # #     return [element for element in range(1000000000)]  # 1.000.000.000
# # #
# # #
# # # def get_numbers():
# # #     for element in range(10):
# # #         yield element
# # #
# # #
# # # # my_sequence = get_numbers()
# # # # for _ in my_sequence:
# # # #     pass
# # #
# # # # my_sequence = get_numbers()
# # # # for element in my_sequence:
# # # #     print(element)
# # # print(next(my_sequence))
# #
# #
# # # def get_numbers():
# # #     return (element for element in range(10))
# #
# # # import sys
# # #
# # # my_list = [element for element in range(1000000)]
# # # print(type(my_list), sys.getsizeof(my_list))
# # # my_generator = (element for element in range(1000000))
# # # print(type(my_generator), sys.getsizeof(my_generator))
# #
# # import os
# #
# # # if __name__ == "__main__":
# # #     # file = open("/home/mihaitzzza/work/siit/nt-15-python/generators_and_files/data", "r")
# # #     # file = open(r"C:\Users\Desktop\data", "r")
# # #     # file = open("C:\\Users\\Desktop\\data", "r")
# # #     file = open("data", "r")
# # #     line = file.readline()
# # #     print(line)
# # #     line = file.readline()
# # #     print(line)
# # #     file.close()
# # #
# # #     file1 = open("data", "w")
# # #     file1.write("custom data from main.py")
# # #
# # #     os.remove("data")
# # #
# # #     line = file.readline()
# # #     print(line)
# # #
# # #     line = file.readline()
# # #     print(line)
# # #
# # #     line = file.readline()
# # #     print(line)
# #
# # # if __name__ == '__main__':
# # #     with open("data") as file:
# # #         line = file.readline()
# # #         print('line', line)
# # #
# # #     line = file.readline()
# # #     print('line', line)
# #
# #
# # # if __name__ == '__main__':
# # #     with open("data") as file:
# # #         content = file.read()
# # #
# # #     print(content)
# #
# #
# # # if __name__ == '__main__':
# # #     with open("data") as file:
# # #         # lines = file.readlines()
# # #         lines = (line for line in file.readlines())
# # #
# # #     print(type(lines))
# # #     for line in lines:
# # #         print(line.replace("\n", ""))
# #
# # # if __name__ == '__main__':
# # #     with open("data", "w") as file:
# # #         # file.write("Hello, World!")
# # #         file.writelines([
# # #             "Hello, World! 1\n",
# # #             "Hello, World! 1\n",
# # #             "Hello, World! 1\n",
# # #             "Hello, World! 1\n",
# # #             "Hello, World! 1\n",
# # #             "Hello, World! 1\n",
# # #             "Hello, World! 1\n",
# # #             "Hello, World! 1\n",
# # #             "Hello, World! 1\n",
# # #             "Hello, World! 1\n",
# # #         ])
# #
# # if __name__ == '__main__':
# #     with open("data", "a") as file:
# #         file.write("Append line #1\n")
# #         file.writelines([
# #             "Append line #2\n",
# #             "Append line #3\n",
# #             "Append line #4\n",
# #         ])
#
# # if __name__ == '__main__':
# #     with open("luceafarul_in") as f:
# #         lines = (line for line in f.readlines())
# #
# #     content = ["STROFA 1\n"]
# #     count = 2
# #     for line in lines:
# #         if line == "\n":
# #             content.append(f"\nSTROFA {count}\n")
# #             count += 1
# #         else:
# #             content.append(line)
# #
# #     with open("luceafarul_in", "w") as f:
# #         f.writelines(content)
#
# if __name__ == '__main__':
#     with open("luceafarul_in", "rb") as f:
#         content = f.read()
#
#     # show original content (string / ASCII data)
#     print(content.decode())  # content.encode() => transforms a string to a binary data (bytearray).

# if __name__ == '__main__':
#     with open("data.csv") as f:
#         lines = (line for line in f.readlines())
#
#     data = []
#     header = []
#     for line in lines:
#         line = line.replace("\n", "")
#         line = line.split(",")
#
#         if not header:
#             header = line
#         else:
#             data.append(line)
#
#     students = [
#         {
#             key: value
#             for key, value in zip(header, student_data)
#         }
#         for student_data in data
#     ]
#     print('students', students)

# import csv
#
# if __name__ == '__main__':
#     with open("data.csv") as f:
#         rows = (row for row in csv.reader(f))
#
#         data = []
#         header = []
#         for row in rows:
#             if not header:
#                 header = row
#             else:
#                 data.append(row)
#
#         students = [
#             {
#                 key: value
#                 for key, value in zip(header, student_data)
#             }
#             for student_data in data
#         ]
#         print('students', students)


# import csv
#
# if __name__ == '__main__':
#     # with open("data.csv") as f:
#     #     dict_reader = csv.DictReader(f)
#     #     students = list(dict_reader)
#     # print(students)
#
#     # data = [
#     #     {"color": "red", "price": 200},
#     #     {"color": "green", "price": 100},
#     #     {"color": "blue", "price": 100},
#     # ]
#     # with open("data-out", "w") as f:
#     #     dict_writer = csv.DictWriter(f, fieldnames=["color", "price"])
#     #     dict_writer.writeheader()
#     #     dict_writer.writerows(data)
#
#     with open("data.csv") as f:
#         dict_reader = csv.DictReader(f)
#         students = list(dict_reader)
#
#     with open("data-out.csv", "w") as f:
#         header = students[0].keys()
#         dict_writer = csv.DictWriter(f, fieldnames=header)
#         dict_writer.writeheader()
#         dict_writer.writerows(students)


import json

if __name__ == '__main__':
    with open("data.json") as f:
        data = json.load(f)

    with open("data-out.json", "w") as f:
        json.dump(data, f, indent=4)
