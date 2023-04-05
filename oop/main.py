class Person:
    def __init__(self, first_name, last_name):
        # print("Constructor for Person class called!", id(self))
        self.first_name = first_name
        self.last_name = last_name

    def intro_to_all(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}!")

    def intro_to_someone(self, other_person: "Person"):
        print("Hello {} {}, my name is {} {}!".format(
            other_person.first_name,
            other_person.last_name,
            self.first_name,
            self.last_name
        ))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


if __name__ == '__main__':
    # popescu_ion = Person("Popescu", "Ion")
    # # print(popescu_ion.first_name, popescu_ion.last_name)
    # # popescu_ion.intro_to_all()
    #
    # print('\n')
    #
    # george_dinel = Person("George", "Dinel")
    # # print(george_dinel.first_name, george_dinel.last_name)
    # # george_dinel.intro_to_all()
    # # george_dinel.intro_to_someone(popescu_ion)

    # person = Person("Popescu", "Ion")
    # print(person)
    # print(person.first_name)
    # print(person.last_name)
    #
    # print("\n")
    #
    # person.first_name = "Gheorghe"
    # person.last_name = "Marian"
    # print(person)
    # print(person.first_name)
    # print(person.last_name)
    # person.intro_to_all()

    # person = Person("Popescu", "Ion")
    # # del person.first_name
    # # print(person.first_name)  # AttributeError
    # if hasattr(person, "first_name"):
    #     print(person.first_name)
    # else:
    #     print("Person has no first_name attribute.")

    person = Person("Popescu", "Ion")
    person.something()  # AttributeError: 'Person' object has no attribute 'something'
