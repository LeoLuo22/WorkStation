# -*- coding:utf-8 -*-

import abc

class Appliance(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, model, price):
        self.__model = model
        sef.price = price

    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

    price = abc.abstractproperty(get_price, set_price)

    @property
    def model(self):
        return self.__model

class Cooker(Appliance):
    def __init__(self, model, price, fuel):
        super().__init__(model, price)
        self.fuel = fuel
        price = property(lambda self: super().price, lambda self, price: super().set_price(price))

