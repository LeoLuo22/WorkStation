from enum import Enum
import time

PizzaProgress = Enum("PizzaProgress", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSource = Enum("PizzaSauce", "tomato creme_fraiche")
PizzaTopping = Enum("PizzaTopping", "mozzarella double_mozzarella bacon ham mushrooms red_onion oregano")
STEP_DELAY = 3

class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print("preparing the {0} dough of your {1}...".format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print("done with the {0} dough.".format(self.dough.name))

class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza("margarita")
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print("adding the tomato sauce to your margarita...")
        self.pizza.sauce = PizzaSource.tomato
        time.sleep(STEP_DELAY)
        print("done with the tomato sauce")

    def add_topping(self):
        print("adding the topping (double mo) to...")
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozzarella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print("done with the topping (double)")

    def bake(self):
        self.progress = PizzaProgress.baking
        print("baking your mar for {} second".format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print("ready")

class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, bulider):
        self.builder = builder
        [step() for step in (builder.prepare_dough, builder.add_sauce, builder.add_topping, builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza
