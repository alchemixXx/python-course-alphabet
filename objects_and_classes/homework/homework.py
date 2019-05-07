"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""
from constants import CARS_TYPES, CARS_PRODUCER, TOWNS
from constants import NAMES
import random
import uuid
import re
from typing import List
import itertools


class Car:

    def __init__(self, price: float, mileage: float, producer, car_type, garage_numb=None):
        self.price = float(price)
        self.number = uuid.uuid4()
        self.mileage = float(mileage)
        self.garage_numb = garage_numb
        self.producer = self.producer_checking(producer)
        self.car_type = self.type_checking(car_type)

    @staticmethod
    def type_checking(car_type):
        if car_type in CARS_TYPES:
            return car_type
        else:
            print("Type should be instance of CAR_TYPES!")

    @staticmethod
    def producer_checking(producer):
        if producer in CARS_PRODUCER:
            return producer
        else:
            print("Producer should be instance of CARS_PRODUCER!")

    def change_number(self, new_number):
        # if re.search('[\w]{8}-[\w]{4}-4[\w]{3}-[\w][\w]{3}-[\w]{12}', new_number):
        # if uuid.UUID(new_number, version=4):
        #     self.number = new_number
        #     return "Number has been changed"
        # else:
        #     return 'Sorry, you have entered wrong number'
        #     # raise ValueError
        try:
            uuid.UUID(new_number, version=4)
            self.number = new_number
            return "Number has been changed"
        except ValueError or AttributeError or TypeError:
            return 'Sorry, you have entered wrong number'

    def __repr__(self):
        return f'"{vars(self)}"'

    def __str__(self):
        return f"""
        'This car has next attributes:
        price="{self.price}",
        type="{self.car_type}",
        number="{self.number}",
        mileage="{self.mileage}",
        garage number = "{self.garage_numb}"'
        """

    def __le__(self, other):
        return self.price <= other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __eq__(self, other):
        return self.price == other.price


class Garage:
    cars = List[Car]
    garage_number = itertools.count()

    def __init__(self, places: int, town, *cars, owner=None):
        self.places = int(places)
        self.owner = self.owner_checking(owner)
        self.number = next(Garage.garage_number)
        self.cars = self.cars_checking(cars)
        self.town = self.town_checking(town)

    @staticmethod
    def owner_checking(owner):
        # if owner is None:
        #     return owner
        # elif re.search('[\w]{8}-[\w]{4}-4[\w]{3}-[\w][\w]{3}-[\w]{12}', owner):
        #     return owner
        # else:
        #     print("Owner should be UUID!")
            # return None

        if owner is None:
            return owner
        else:
            try:
                uuid.UUID(owner, version=4)
                return owner
            except ValueError or AttributeError or TypeError:
                print("Owner should be UUID!")

    @staticmethod
    def town_checking(town):
        if town in TOWNS:
            return town
        else:
            print("Town should be instance of TOWNS!")
            # return None

    def cars_checking(self, cars):
        actual_cars = list()
        for car in cars:
            if car.garage_numb is None:
                actual_cars.append(car)
                car.garage_numb = self.number
            else:
                print(f"Car {car} is already in garage {car.garage_numb}")
                continue
        if len(actual_cars) <= self.places:
            return actual_cars
        else:
            print(f"Come on, guys! It's too much for this garage. It can contain only {self.places} cars")
    #
    # def all_cars(self):
    #     return [car for car in self.cars]

    def add(self, car):
        if self.free_places() > 0:
            if car.garage_numb is None:
                car.garage_numb = self.garage_number
                self.cars.append(car)
                return "Car has been added"
            else:
                print("This car is already in other garage")
        else:
            print("Sorry, this garage is full. Car has not been changed")
            # raise ValueError

    def remove(self, car):
        if car in self.cars:
            car.garage_numb = None
            self.cars.remove(car)
            return "Car has been removed"
        else:
            print("Sorry, there is no that car in the garage")
            # raise ValueError

    def hit_hat(self):
        return sum([car.price for car in self.cars])

    def change_owner(self, owner_id):
        try:
            uuid.UUID(owner_id, version=4)
            self.owner = owner_id
        except ValueError or AttributeError or TypeError:
            print("Sorry, it's not UUID. Owner has not been changed")
        # if re.search('[\w]{8}-[\w]{4}-4[\w]{3}-[\w][\w]{3}-[\w]{12}', owner_id):
        #     self.owner = owner_id
        # else:
        #     print("Sorry, it's not UUID. Owner has not been changed")
            # raise ValueError

    def free_places(self):
        return self.places - len(self.cars)

    def __str__(self):
        return f"""Garage {self.number} has next attributes:
        cars =  '{len(self.cars)} cars', 
        owner = '{self.owner}',
        town = '{self.town}',
        number = '{self.number}',
        free places = {self.free_places()}
        """

    def __repr__(self):
        return f'"{vars(self)}"'


class Cesar:
    garages = List[Garage]

    def __init__(self, name, *garages):
        self.name = name
        self.register_id = uuid.uuid4()
        self.garages = self.garages_checking(garages)

    # @staticmethod
    # def garages_checking(garages):
    #     if len(garages) > 0:
    #         return garages
    #     else:
    #         return []

    def garages_checking(self, garages):
        if len(garages) > 0:
            real_garages = list()
            for garage in garages:
                if garage.owner is None or garage.owner == self.register_id:
                    garage.change_owner(str(self.register_id))
                    real_garages.append(garage)
                else:
                    print("Other cesar own this garage")
            return real_garages
        else:
            return []

    def garages_count(self):
        return len(self.garages)

    def hit_hat(self):
        return sum([sum([car.price for car in garage.cars]) for garage in self.garages])
        # total_price = 0
        # for garage in self.garages:
        #     for car in garage.cars:
        #         total_price += car.price
        # return total_price

    def cars_count(self):
        return sum([len(garage.cars) for garage in self.garages])

    def add_car(self, car, chosen_garage=None):
        if chosen_garage is None:
            def max_free():
                all_garages = {garage.number: (garage.places - len(garage.cars)) for garage in self.garages}
                max_free_garage = {key: value for (key, value) in all_garages.items() if
                                   value == max(all_garages.values())}

                if max_free_garage.values() != 0:
                    return max_free_garage
                else:
                    return "Sorry, there is no free places in the garages"

            most_empty_garage = max_free()
            if most_empty_garage is isinstance(most_empty_garage, str):
                return most_empty_garage
            else:
                for garage in self.garages:
                    if garage.number == [x for x in most_empty_garage.keys()][0]:
                        garage.add(car)
                        return f"Car has been added to garage {garage.number}"
        elif chosen_garage in self.garages:
            if chosen_garage.free_places() >= 0:
                chosen_garage.add(car)
                return f"Car has been added to garage {chosen_garage}"
            else:
                return f"Sorry, there is no free places in the garage {chosen_garage}"
        else:
            print("Get out of here! It's not your garage!")

    def __str__(self):
        return (f"""This Cesar has next attributes:
        name = '{self.name}',
        id = '{self.register_id}',
        number of garages = {self.garages_count()}""")

    def __repr__(self):
        return f'"{vars(self)}"'

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __ge__(self, other):
        return self.hit_hat() >= other.hit_hat()

    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()


if __name__ == '__main__':
    car1 = Car(random.randrange(100, 1000), random.randrange(100, 2000), random.choice(CARS_PRODUCER),
               random.choice(CARS_TYPES))
    car2 = Car(random.randrange(100, 1000), random.randrange(100, 2000), random.choice(CARS_PRODUCER),
               random.choice(CARS_TYPES))
    car3 = Car(random.randrange(100, 1000), random.randrange(100, 2000), random.choice(CARS_PRODUCER),
               random.choice(CARS_TYPES))
    car4 = Car(random.randrange(100, 1000), random.randrange(100, 2000), random.choice(CARS_PRODUCER),
               random.choice(CARS_TYPES))
    car5 = Car(random.randrange(100, 1000), random.randrange(100, 2000), random.choice(CARS_PRODUCER),
               random.choice(CARS_TYPES))
    car6 = Car(random.randrange(100, 1000), random.randrange(100, 2000), random.choice(CARS_PRODUCER),
               random.choice(CARS_TYPES))
    car7 = Car(random.randrange(100, 1000), random.randrange(100, 2000), random.choice(CARS_PRODUCER),
               random.choice(CARS_TYPES))
    car8 = Car(random.randrange(100, 1000), random.randrange(100, 2000), random.choice(CARS_PRODUCER),
               random.choice(CARS_TYPES))
    car9 = Car(random.randrange(100, 1000), random.randrange(100, 2000), random.choice(CARS_PRODUCER),
               random.choice(CARS_TYPES))
    car10 = Car(random.randrange(100, 1000), random.randrange(100, 2000), random.choice(CARS_PRODUCER),
                random.choice(CARS_TYPES))

    garage1 = Garage(random.randrange(5, 150), random.choice(TOWNS), car1, car2)

    garage2 = Garage(random.randrange(5, 150), random.choice(TOWNS), car3)

    garage3 = Garage(random.randrange(5, 150), random.choice(TOWNS), car4, car5)

    garage4 = Garage(random.randrange(5, 150), random.choice(TOWNS), car6, car7,
                     owner=str(uuid.uuid4()))

    garage5 = Garage(random.randrange(5, 150), random.choice(TOWNS), car8, car9,
                     owner=str(uuid.uuid4()))

    cesar_1 = Cesar(random.choice(NAMES), garage1, garage3)
    cesar_2 = Cesar(random.choice(NAMES), garage2)
    cesar_3 = Cesar(random.choice(NAMES), garage4, garage5)

    new_id_correct = "c90cb2a4-33d2-427d-8876-ba7ed1cb3fc6"
    # new_id_correct = uuid.uuid4()
    new_id_wrong = " 33d2-427d-8876-ba7ed1cb3fc6 "
    print("Testing Car class:")
    print(car1)
    print(car2)
    print(car1 > car2)
    print(car1 >= car2)
    print(car1 == car2)
    print(car1 <= car2)
    print(car1 <= car2)

    print(car1.change_number(new_id_correct))
    print(car1.change_number(new_id_wrong))

    print('\n' * 5)
    print("Testing Garage class:")
    print(garage1)
    print(garage2)
    print(garage3)

    print("This is hit_hat method", garage1.hit_hat())

    print(garage1.add(car10))
    print(garage1)
    print(garage1.remove(car10))
    print(garage1)
    print("This is free_spaces method", garage1.free_places())

    print('\n' * 5)
    print("Testing Cesar class:")

    print(cesar_1)
    print(cesar_2)

    print("Testing garages after creating cesars")
    print(garage1)
    print(garage2)
    print(garage3)

    print("This is hit_hat method", cesar_1.hit_hat())
    print("This is cars_count method", cesar_1.cars_count())
    print("This is garage_count method", cesar_1.garages_count())

    print("This is add_car method with garage specification", cesar_1.add_car(car10, garage1))
    print(garage1.remove(car10))
    print("This is add_car method without garage specification", cesar_1.add_car(car10))
