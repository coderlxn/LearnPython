# -*- coding: utf-8 -*-
# @Time    : 11/21/18 11:42 AM
# @Author  : Jax.Li
# @FileName: abstract_factory.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import random

factory_list = []


def randomly(cls):
    print("app class {} to factory list".format(cls))
    factory_list.append(cls)
    return cls


class PetShop(object):
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory()
        print("We have a lovely {}".format(pet))


@randomly
class Dog(object):
    def speek(self):
        return 'woof'

    def __str__(self):
        return "Dog"


@randomly
class Cat(object):
    def speek(self):
        return "meow"

    def __str__(self):
        return "Cat"


def random_animal():
    return random.choice(factory_list)()


if __name__ == '__main__':
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()

    shop = PetShop(random_animal)
    for i in range(3):
        shop.show_pet()
        print("=" * 20)
