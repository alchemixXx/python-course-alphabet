from __future__ import annotations

"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""


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
from typing import List
import itertools
import json
from ruamel.yaml import YAML
import pickle
from pprint import pprint


class Car:

    def __init__(self, price: float, mileage: float, producer, car_type, garage_numb=None, number=None):
        self.price = float(price)
        self.number = uuid.uuid4() if number is None else number
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

    # JSON serialization part
    def convert_to_dict(obj):

        #  Populate the dictionary with object meta data
        obj_dict = {
            "__class__": obj.__class__.__name__,
            "__module__": obj.__module__
        }

        #  Populate the dictionary with object properties
        obj_dict.update(obj.__dict__)

        return obj_dict

    @classmethod
    def from_json(cls):
        pass

    def change_number(self, new_number):
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

    def __init__(self, places: int, town, *cars, owner=None, number=None):
        self.places = int(places)
        self.owner = self.owner_checking(owner)
        self.number = next(Garage.garage_number) if number is None else number
        self.cars = self.cars_checking(cars)
        self.town = self.town_checking(town)

    @staticmethod
    def owner_checking(owner):
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

    def remove(self, car):
        if car in self.cars:
            car.garage_numb = None
            self.cars.remove(car)
            return "Car has been removed"
        else:
            print("Sorry, there is no that car in the garage")

    def hit_hat(self):
        return sum([car.price for car in self.cars])

    def change_owner(self, owner_id):
        try:
            uuid.UUID(owner_id, version=4)
            self.owner = owner_id
        except ValueError or AttributeError or TypeError:
            print("Sorry, it's not UUID. Owner has not been changed")

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

# JSON SERIALIZATION
class JsonConverter(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        if isinstance(obj, Car):
            return {"__class__": obj.__class__.__name__,
                    "__module__": obj.__module__,
                    'price': obj.price, 'mileage': obj.mileage,
                    'producer': obj.producer,
                    'car_type': obj.car_type,
                    'garage_numb': obj.garage_numb,
                    'number': obj.number}
        if isinstance(obj, Garage):
            return {"__class__": obj.__class__.__name__,
                    "__module__": obj.__module__,
                    'places': obj.places,
                    'owner': obj.owner,
                    'number': obj.number,
                    # 'cars': obj.cars,
                    'cars': [self.default(inst) for inst in obj.cars],
                    'town': obj.town}
        if isinstance(obj, Cesar):
            return {"__class__": obj.__class__.__name__,
                    "__module__": obj.__module__,
                    'name': obj.name,
                    'register_id': obj.register_id,
                    'garages': obj.garages}
        return json.JSONEncoder.default(self, obj)

# name = data['name']
# language = data['language']
# position = data['position']
# pr = Programmer(name=name, language=language, position=position)
# pr.enough_coffee = data.get('enough_coffee', False)
# # return pr
#
#     def __init__(self, price: float, mileage: float, producer, car_type, garage_numb=None, number=None):
#         self.price = float(price)
#         self.number = uuid.uuid4() if number is None else number
#         self.mileage = float(mileage)
#         self.garage_numb = garage_numb
#         self.producer = self.producer_checking(producer)
#         self.car_type = self.type_checking(car_type)


def car_deserial(obj):
    price = obj['price']
    mileage = obj['mileage']
    producer = obj['producer']
    car_type = obj['car_type']
    garage_numb = obj['garage_numb']
    number = uuid.UUID(obj['number'], version=4)
    car = Car(price=price, mileage=mileage, producer=producer, car_type=car_type,
              garage_numb=garage_numb, number=number)
    return car


def garage_deserial(obj):
    places = obj['places']
    owner = obj['owner']
    number = obj['number']
    # cars = [car_deserial(car) for car in obj['cars']]
    cars = obj['cars']
    town = obj['town']
    garage = Garage(places, town, *cars, owner=owner, number=number)
    return garage

def cesar_deserial(obj):
    pass
    cesar = Cesar(places, town, cars, owner=owner, number=number)
    return cesar


def json_hook(obj):
    if obj['__class__'] == "Car":
        return car_deserial(obj)
    elif obj['__class__'] == "Garage":
        return garage_deserial(obj)
    elif obj['__class__'] == "Cesar":
        return cesar_deserial(obj)

# def json_hook(obj):
#     if "__class__" in obj:
#         class_name = obj.pop("__class__")
#         module_name = obj.pop("__module__")
#         module = __import__(module_name)
#         class_ = getattr(module, class_name)
#         obj = class_(**obj)
#     else:
#         obj = obj
#     return obj


# PICKLE SERIALIZATION


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

    # JSON SERIALIZATION
    json_serialized_car = json.dumps(car1, cls=JsonConverter, indent=4)
    # serialized_car = json.dumps(car1.convert_to_dict(), indent=4)
    json_serialized_garage = json.dumps(garage1, cls=JsonConverter, indent=4)
    json_serialized_cesar = json.dumps(cesar_1, cls=JsonConverter, indent=4)


    print("!!!JSON SERIALIZATION ZONE!!!")
    print("Car serialization:")
    print(json_serialized_car)
    print('\n'*5)
    print("Garage serialization:")
    print(json_serialized_garage)
    print('\n'*5)
    print("Cesar serialization:")
    print(json_serialized_cesar)
    print('\n'*5)



    print("!!! JSON DESERIALIZATION ZONE!!!")
    des_car1 = json.loads(json_serialized_car, object_hook=json_hook)
    print("This is original car")
    print(car1)
    print("This is car after deserialization")
    print(des_car1)
    # print(type(des_car1.price))
    # print(type(des_car1.mileage))
    print('\n'*5)
    des_gar1 = json.loads(json_serialized_garage, object_hook=json_hook)
    print("This is original garage")
    print(garage1)
    print("This is garage after deserialization")
    print(des_gar1)
    print(type(des_gar1))
    # print(des_gar1[0])
    # print(type(des_gar1[0]))

# # PICKLE SERIALIZATION
#     pickle_serialized_car = pickle.dumps(car1)
#     # serialized_car = json.dumps(car1.convert_to_dict(), indent=4)
#     pickle_serialized_garage = pickle.dumps(garage1)
#     pickle_serialized_cesar = pickle.dumps(cesar_1)


    # print("!!!S PICKLE ERIALIZATION ZONE!!!")
    # print("Car serialization:")
    # print(pickle_serialized_car)
    # print('\n'*5)
    # print("Garage serialization:")
    # print(pickle_serialized_garage)
    # print('\n'*5)
    # print("Cesar serialization:")
    # print(pickle_serialized_cesar)
    # print('\n'*5)
    #
    #
    #
    # print("!!!PICKLE DESERIALIZATION ZONE!!!")
    # des_car2 = pickle.loads(pickle_serialized_car)
    # print("This is original car")
    # print(car1)
    # print("This is car after deserialization")
    # print(des_car1)
    # # print(type(des_car1.price))
    # # print(type(des_car1.mileage))
    # print('\n'*5)
    # des_gar2 = pickle.loads(pickle_serialized_garage)
    # print("This is original garage")
    # print(garage1)
    # print("This is garage after deserialization")
    # print(des_gar1)
    # print(type(des_gar1))
    # # print(des_gar1[0])
    # # print(type(des_gar1[0]))

