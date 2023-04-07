# # # class Person:
# # #     def __init__(self, first_name, last_name):
# # #         # print("Constructor for Person class called!", id(self))
# # #         self.first_name = first_name
# # #         self.last_name = last_name
# # #
# # #     def intro_to_all(self):
# # #         print(f"Hello, my name is {self.first_name} {self.last_name}!")
# # #
# # #     def intro_to_someone(self, other_person: "Person"):
# # #         print("Hello {} {}, my name is {} {}!".format(
# # #             other_person.first_name,
# # #             other_person.last_name,
# # #             self.first_name,
# # #             self.last_name
# # #         ))
# # #
# # #     def __str__(self):
# # #         return f"{self.first_name} {self.last_name}"
# # #
# # #
# # # if __name__ == '__main__':
# # #     # popescu_ion = Person("Popescu", "Ion")
# # #     # # print(popescu_ion.first_name, popescu_ion.last_name)
# # #     # # popescu_ion.intro_to_all()
# # #     #
# # #     # print('\n')
# # #     #
# # #     # george_dinel = Person("George", "Dinel")
# # #     # # print(george_dinel.first_name, george_dinel.last_name)
# # #     # # george_dinel.intro_to_all()
# # #     # # george_dinel.intro_to_someone(popescu_ion)
# # #
# # #     # person = Person("Popescu", "Ion")
# # #     # print(person)
# # #     # print(person.first_name)
# # #     # print(person.last_name)
# # #     #
# # #     # print("\n")
# # #     #
# # #     # person.first_name = "Gheorghe"
# # #     # person.last_name = "Marian"
# # #     # print(person)
# # #     # print(person.first_name)
# # #     # print(person.last_name)
# # #     # person.intro_to_all()
# # #
# # #     # person = Person("Popescu", "Ion")
# # #     # # del person.first_name
# # #     # # print(person.first_name)  # AttributeError
# # #     # if hasattr(person, "first_name"):
# # #     #     print(person.first_name)
# # #     # else:
# # #     #     print("Person has no first_name attribute.")
# # #
# # #     person = Person("Popescu", "Ion")
# # #     person.something()  # AttributeError: 'Person' object has no attribute 'something'
# #
# #
# # class Person:
# #     def __init__(self, first_name, last_name):
# #         self.__first_name = first_name
# #         self.__last_name = last_name
# #
# #     # def get_first_name(self):
# #     #     # ... validate who's accessing the property
# #     #     return self.__first_name
# #     #
# #     # def set_first_name(self, new_value):
# #     #     # ... validate who's accessing the property
# #     #     self.__first_name = new_value
# #
# #     @property
# #     def first_name(self):
# #         # ... validate who's accessing the property
# #         # raise Exception("You do not have access to this property!")
# #         # print("PROPERTY GETTER IS CALLED HERE!!!!")
# #         return self.__first_name
# #
# #     @first_name.setter
# #     def first_name(self, new_value):
# #         # ... validate who's accessing the property
# #         self.__first_name = new_value
# #
# #     @property
# #     def full_name(self):
# #         return f"{self.__first_name} {self.__last_name}"
# #
# #     # @full_name.setter
# #     # def full_name(self, new_value):
# #     #     self.__first_name = new_value.split(" ")[0]
# #     #     self.__last_name = new_value.split(" ")[1]
# #
# #
# #     def __str__(self):
# #         return f"{self.__first_name} {self.__last_name}"
# #
# #
# # if __name__ == '__main__':
# #     # person = Person("Ion", "Popescu")
# #     # person.set_first_name("Gigel")
# #     # print(person.get_first_name())
# #
# #     # NAME MANGLING
# #     # person._Person__first_name = "Gigel"
# #     # print(person._Person__first_name)
# #
# #     person = Person("Ion", "Popescu")
# #     # person.set_first_name("Gigel")
# #     # print(person.get_first_name())
# #     # person.first_name = "Gigel"
# #     # print(person.first_name, f"(correct name: {person.get_first_name()})")
# #     # person.first_name = "Gigel"
# #     # print(person.first_name)
# #     # person.full_name = "Gigel Dobre"
# #     # print(person.full_name)
# #     # print(person.first_name)
# #     # print(person._Person__last_name)
#
# # class A:
# #     def __a_method(self):
# #         print("This is 'a_method' from 'A' class")
# #
# #
# # a = A()
# # a._A__a_method()
#
#
# # class Dog:
# #     legs_no = 4
# #
# #     def __init__(self, name, bread):
# #         self.name = name
# #         self.bread = bread
# #
# #     def __str__(self):
# #         return self.name
# #
# #
# # # rex = Dog("Rex", "bulldog")
# # # print(rex)
# # # print("legs_no", rex.legs_no)
# # print(Dog.legs_no)
#
# # import random
# #
# # class A:
# #     x = 10
# #
# #     def __init__(self):
# #         self.x = random.choice(["a", "b", "c"])
# #
# #
# # a1 = A()
# # a2 = A()
# # print("a1.x", a1.x)
# # print("a2.x", a2.x)
# #
# # A.x = 20
# #
# # print("A.x", A.x)
# # print(a1.x)
# # print(a2.x)
#
#
# class Dog:
#     legs_no = 4
#
#     def __init__(self, name, bread):
#         self.name = name
#         self.bread = bread
#
#     # def speak(self):
#     #     print(f"{self.name} barks!")
#     @staticmethod
#     def speak():
#         print("Ham, ham!")
#
#     def __str__(self):
#         return self.name
#
#
# # rex = Dog("Rex", "bulldog")
# # rex.speak()
# #
# # ben = Dog("Ben", "bulldog")
# # ben.speak()
#
# Dog.speak()

# Composition
class City:
    def __init__(self, name, population, country):
        self.name = name
        self.population = population
        self.country = country

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class Country:
    def __init__(self, name):
        self.name = name
        self.flag = None
        self.cities = []

    @property
    def population(self):
        return sum(city.population for city in self.cities)

    # def set_cities(self, cities):
    #     self.cities = cities
    def add_cities(self, cities):
        self.cities.extend(cities)

    def __str__(self):
        return self.name


romania = Country("Romania")

sibiu = City("Sibiu", 300000, romania)
iasi = City("Iasi", 250000, romania)

romania.add_cities([sibiu, iasi])


# print(romania.name, romania.population)

# print(romania.cities)
# print(sibiu.country, iasi.country)

print(sibiu.country.cities[0].country.cities[1].country.cities)

