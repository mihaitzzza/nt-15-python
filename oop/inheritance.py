class Passport:
    def __init__(self, series, number):
        self.__series = series
        self.__number = number

    @property
    def series(self):
        return self.__series

    @property
    def number(self):
        return self.__number


class Animal:
    def __init__(self, name, passport=None, age=0):
        self._name = name
        self._passport = passport
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def passport(self):
        return self._passport

    @passport.setter
    def passport(self, new_passport):
        self._passport = new_passport

    @property
    def age(self):
        return self._age

    def gets_old(self):
        self._age += 1

    def _speak(self, dialect):
        print(f"{type(self).__name__} {self._name}: '{dialect}'")


class Mammal(Animal):
    def get_birth(self):
        print(f"{type(self)} - {self._name}: Born alive children.")


class Bird(Animal):
    def get_birth(self):
        print(f"{type(self)} - {self._name}: Lay down eggs.")


class Cat(Mammal):
    def speak(self):
        super()._speak('Miau! Miau!')


class Dog(Mammal):
    def speak(self):
        super()._speak('Ham! Ham!')


class Pig(Mammal):
    def speak(self):
        super()._speak('Oink! Oink!')


class Perrot(Bird):
    def speak(self):
        super()._speak('Cirip! Cirip!')


class Tiger(Mammal):
    def speak(self):
        super()._speak('Roooaaar!')


class Whale(Mammal):
    def speak(self):
        super()._speak('Aaaaaoooooaaaooo!')


class Dolphin(Mammal):
    pass


if __name__ == '__main__':
    # micky_cat = Cat("Micky", passport=Passport(series="A123", number="20230425000"))
    # misha_dog = Dog("Misha")
    # viorel_pig = Pig("Viorel")
    # coco_perrot = Perrot("Coco")
    # julie_cat = Cat("Julie")
    #
    # animals = [
    #     micky_cat,
    #     misha_dog,
    #     viorel_pig,
    #     coco_perrot,
    #     julie_cat
    # ]

    # # 2 years later...
    # for animal in animals:
    #     animal.gets_old()
    #     animal.gets_old()
    #
    # misha_dog.passport = Passport(series="A124", number="20230425001")
    #
    # for animal in animals:
    #     # print(type(animal), animal.passport, animal.age)
    #     animal.get_birth()
    #     print(animal._name)

    micky_cat = Cat("Micky", passport=Passport(series="A123", number="20230425000"))
    misha_dog = Dog("Misha")
    viorel_pig = Pig("Viorel")
    coco_perrot = Perrot("Coco")
    julie_cat = Cat("Julie")
    simba_tiger = Tiger("Simba")
    flipper_whale = Whale("Flipper")
    rex_dolphin = Dolphin("Rex")

    animals = [
        micky_cat,
        misha_dog,
        viorel_pig,
        coco_perrot,
        julie_cat,
        simba_tiger,
        flipper_whale,
        rex_dolphin,
    ]

    for animal in animals:
        animal.speak()
