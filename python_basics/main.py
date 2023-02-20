# # # varsta_copil_mic = 10
# # # varsta_copil_mare = 12
# # #
# # # print(varsta_copil_mic, varsta_copil_mare)
# # # print("copil mic = ", varsta_copil_mic)
# # # print("copil mare = ", varsta_copil_mare)
# #
# # # nr_1 = 5
# # # nr_2 = 2
# # # # nr_3 = 7 + 8
# # # # nr_3 = nr_1 + 2
# # # # nr_3 = nr_1 + nr_2
# # #
# # # nr_3 = nr_1 % nr_2 == 1
# # #
# # # print('nr_3', nr_3)
# #
# # # a = 10
# # # print('a', a)
# # # print('id(a)', id(a))
# #
# # # a = 3
# # # print('a', a)
# # # a = a + 5
# # # print('a', a)
# # # b = 4
# #
# # # a = 4
# # # print(a, type(a))
# # #
# # # # a = True
# # # # print(a, type(a))
# # #
# # # a = 8
# # # print(a, type(a))
# #
# # # wfhisfhuis = None  # null -> from other languages
# #
# # # boy_name = "Mihai"
# # # girl_name = 'Ana'
# # # print(boy_name, girl_name)
# #
# # # a = ""
# # # print("_", a, "_")
# # # print(type(a))
# #
# # # a = "a"
# # # print(a, type(a))
# #
# # # message = 'Mihai a zis "Buna ziua!"'
# # # print(message, type(message))  # Mihai a zis "Buna ziua!"
# #
# # # message = 'Mihai, alias \'M\', a zis "Buna ziua!"\\\'Salut!\' Ii raspunde Ionut.'
# # # print(message, type(message))  # Mihai, alias 'M', a zis "Buna ziua!"\'Salut!' Ii raspunde Ionut.
# #
# # # print("Linia 1\n\n\tLinia 2\b")
# # # print("Linia 1\\n\\n\\tLinia 2")  # Linia 1\n\n\tLinia 2
# #
# # # print("Linia 1\n\n\tLinia 2")  # Linia 1\n\n\tLinia 2
# # # do the same using RAW string
# # # print(r"Linia 1\n\n\tLinia 2")
# #
# # # my_age = 27
# # # x = str(my_age)
# # # print(x, type(x))
# #
# # # my_name = "Ionut"
# # # my_age = 27
# # # my_city = "Sibiu"
# # # # message = "My name is Mihai, I am 30 years old and I am living in Craiova."
# # # message = "My name is " + my_name + ", I am " + str(my_age) + " years old and I am living in " + my_city
# # # print(message)
# #
# # name = "Ionut"
# # age = 27
# # city = "Bucuresti"
# # # message = "My name is %s, I am %d years old and I am living in %s." % (my_name, my_age, my_city)
# # # message = "My name is %s, I am %d years old and I am living in %s." % (my_name, my_city, my_age)
# # # message = "My name is {}, I am {} years old and I am living in {}.".format(my_name, my_age, my_city)
# # # message = "My name is {1}, I am {0} years old and I am living in {2}.".format(my_age, my_name, my_city)
# # # #                                                                               0         1       2
# # # message = "My name is {name_1}, I am {my_second_guess} years old and I am living in {bla_bla_bla}.".format(name_1=my_name, bla_bla_bla=my_city, my_second_guess=my_age)
# # # message = "My name is {name}, I am {age} years old and I am living in {city}.".format(name=name, city=city, age=age)
# # # message = "My name is {name}, I am {age} years old and I am living in {city}.".format(age=age, name=name, city=city)
# # # message = "My name is {name}, I am {age} years old and I am living in {city}.".format(name=name, age=age, city=city)
# # message = f"My name is {name}, I am {age} years old and I am living in {city}."  # f-string
# # print(message)
#
# # a = "a"
# # print(a, type(a))
#
# # print("print something in console!")
# # print(type(12), type(12.5), type(12+4j), type(True), type(False), type(None), type("random string"))
# # print(id(12))
#
# # a = 3
# # b = 3
# # print(a == b, a is b)
#
# a = "abc"
# b = "abc"
# c = a
# # print(a == b, a is b)
# print(id(a))
# print(id(b))
# print(id(c))
#
# # a = [1, 2, 3]
# # b = [1, 2, 3]
# # c = a
# # print(a == b, a is b, a is c)
# # print(id(a))
# # print(id(b))
# # print(id(c))

# a = 3
# b = 3.0
# print(a == b, a is b)

a = 7
print(a is 7)
