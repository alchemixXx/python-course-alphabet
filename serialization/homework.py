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

from constants import CARS_TYPES, CARS_PRODUCER, TOWNS
from constants import NAMES
import random
import uuid
from typing import List
import itertools
import json
from ruamel.yaml import YAML
import pickle
import configparser


class Car:

    def __init__(self, price: float, mileage: float, producer, car_type, garage_numb=None, number=None):
        self.price = self._convert_to_float(price)
        self.number = uuid.uuid4() if number is None else number
        self.mileage = self._convert_to_float(mileage)
        self.garage_numb = garage_numb
        self.producer = self.producer_checking(producer)
        self.car_type = self.type_checking(car_type)

    @staticmethod
    def _convert_to_float(value):
        try:
            if value is True or value is False:
                raise TypeError
            return float(value)
        except TypeError:
            return None

    @staticmethod
    def type_checking(car_type):
        if car_type in CARS_TYPES:
            return car_type
        else:
            raise ValueError("Type should be instance of CAR_TYPES!")

    @staticmethod
    def producer_checking(producer):
        if producer in CARS_PRODUCER:
            return producer
        else:
            raise ValueError("Producer should be instance of CARS_PRODUCER!")

    def change_number(self, new_number):
        try:
            uuid.UUID(new_number, version=4)
            self.number = new_number
            return "Number has been changed"
        except AttributeError:
            return 'Sorry, you have entered wrong number. It should be a string, not list, tuple, set, dict, int or float'
        except ValueError:
            return 'Sorry, you have entered bad format of string'
        except TypeError:
            return 'Sorry, you have entered bad type of argument. ' \
                   'One of the hex, bytes, bytes_le, fields, or int arguments must be given'

    def equality(self, other):
        return vars(self) == vars(other)

    # def __repr__(self):
    #     return f'"{vars(self)}"'

    # def __str__(self):
    #     return f"""
    #     'This car has next attributes:
    #     price="{self.price}",
    #     type="{self.car_type}",
    #     number="{self.number}",
    #     mileage="{self.mileage}",
    #     garage number = "{self.garage_numb}"'
    #     """

    def __repr__(self):
        return f'Car(price={self.price}, ' \
            f'producer="{self.producer}", ' \
            f'car_type="{self.car_type}", ' \
            f'number="{self.number}", ' \
            f'mileage={self.mileage}, ' \
            f'garage_numb={self.garage_numb})'

    def __str__(self):
        return f'This car has attributes: {vars(self)}'

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
        self.places = self._to_int(places)
        self.owner = self.owner_checking(owner)
        self.number = next(Garage.garage_number) if number is None else number
        # self.cars = self.cars_checking(cars)
        self.cars = cars

        self.town = self.town_checking(town)

    @staticmethod
    def owner_checking(owner):
        if owner is None:
            return owner
        else:
            try:
                uuid.UUID(owner, version=4)
                return owner
            except AttributeError:
                return 'Sorry, you have entered wrong number. ' \
                       'It should be a string, not list, tuple, set, dict, int or float'
            except ValueError:
                return 'Sorry, you have entered bad format of string'
            except TypeError:
                return 'Sorry, you have entered bad type of argument. ' \
                       'One of the hex, bytes, bytes_le, fields, or int arguments must be given'

    @staticmethod
    def town_checking(town):
        if town in TOWNS:
            return town
        else:
            raise ValueError("Town should be instance of TOWNS!")

    @staticmethod
    def _to_int(value):
        try:
            if value is True or value is False:
                raise TypeError
            return int(value)
        except TypeError:
            return None

    # def cars_checking(self, cars):
    #     actual_cars = list()
    #     for car in cars:
    #         if car.garage_numb is None:
    #             actual_cars.append(car)
    #             car.garage_numb = self.number
    #         else:
    #             print(f"Car {car} is already in garage {car.garage_numb}")
    #             continue
    #     if len(actual_cars) <= self.places:
    #         return actual_cars
    #     else:
    #         print(f"Come on, guys! It's too much for this garage. It can contain only {self.places} cars")

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
        "{vars(self)}"
        """

    def __repr__(self):
        return f"Garage(" \
            f"{self.places}, " \
            f"town='{self.town}," \
            f"{self.cars}, " \
            f"owner='{self.owner}', " \
            f"number={self.number})"




class Cesar:
    garages = List[Garage]

    def __init__(self, name, *garages, register_id=None):
        self.name = name
        self.register_id = uuid.uuid4() if register_id is None else register_id
        self.garages = self.garages_checking(garages)
        # self.garages = self.garages

    def garages_checking(self, garages):
        if len(garages) > 0:
            real_garages = list()
            for garage in garages:
                # if garage.owner is None or garage.owner == self.register_id:
                garage.change_owner(str(self.register_id))
                real_garages.append(garage)
                # else:
                #     print("Other cesar own this garage")
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
                    'price': obj.price,
                    'mileage': obj.mileage,
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
    cars = obj['cars']
    town = obj['town']
    garage = Garage(places, town, *cars, owner=owner, number=number)
    return garage


def cesar_deserial(obj):
    name = obj['name']
    register_id = uuid.UUID(obj['register_id'], version=4)
    garages = obj['garages']
    cesar = Cesar(name, *garages, register_id=register_id)
    return cesar


def json_hook(obj):
    if obj['__class__'] == "Car":
        return car_deserial(obj)
    elif obj['__class__'] == "Garage":
        return garage_deserial(obj)
    elif obj['__class__'] == "Cesar":
        return cesar_deserial(obj)


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

    garage1 = Garage(random.randrange(5, 150), random.choice(TOWNS), car1, car2)

    garage2 = Garage(random.randrange(5, 150), random.choice(TOWNS), car3)

    garage3 = Garage(random.randrange(5, 150), random.choice(TOWNS), car4, car5)

    cesar_1 = Cesar(random.choice(NAMES), garage1, garage3)
    cesar_2 = Cesar(random.choice(NAMES), garage2)

    print(garage1.__repr__())
    print(eval(garage1.__repr__()))


    """Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
    yaml, json, pickle відповідно."""

    """ Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
    з (yaml, json, pickle) строки відповідно"""

    # # JSON SERIALIZATION
    # json_serialized_car = json.dumps(car1, cls=JsonConverter, indent=4)
    # json_serialized_garage = json.dumps(garage1, cls=JsonConverter, indent=4)
    # json_serialized_cesar = json.dumps(cesar_1, cls=JsonConverter, indent=4)
    #
    # # JSON DESERIALIZATION
    # des_car1 = json.loads(json_serialized_car, object_hook=json_hook)
    # des_gar1 = json.loads(json_serialized_garage, object_hook=json_hook)
    # des_ces1 = json.loads(json_serialized_cesar, object_hook=json_hook)
    #
    # # PICKLE SERIALIZATION
    # pickle_serialized_car = pickle.dumps(car1)
    # pickle_serialized_garage = pickle.dumps(garage1)
    # pickle_serialized_cesar = pickle.dumps(cesar_1)
    #
    # # PICKLE DESERIALIZATION
    # des_car2 = pickle.loads(pickle_serialized_car)
    # des_gar2 = pickle.loads(pickle_serialized_garage)
    # des_ces2 = pickle.loads(pickle_serialized_cesar)
    #
    # # # YAML SERIALIZATION
    # # yaml = YAML()
    # # yaml_serialized_car = yaml.dump(car1)
    # # pickle_serialized_garage = pickle.dumps(garage1)
    # # pickle_serialized_cesar = pickle.dumps(cesar_1)
    # #
    # # print(yaml_serialized_car)
    #
    # # print("!!!--------------------JSON SERIALIZATION ZONE-------------------------!!!")
    # # print("Car serialization:")
    # # print(json_serialized_car)
    # # print('\n'*5)
    # # print("Garage serialization:")
    # # print(json_serialized_garage)
    # # print('\n'*5)
    # # print("Cesar serialization:")
    # # print(json_serialized_cesar)
    # # print('\n'*5)
    # #
    # # print("!!! --------------------JSON DESERIALIZATION ZONE--------------------!!!")
    # #
    # # print("This is original car")
    # # print(car1)
    # # print()
    # # print("This is car after deserialization")
    # # print(des_car1)
    # # print('\n'*5)
    # #
    # # print("This is original garage")
    # # print(garage1)
    # # print()
    # # print("This is garage after deserialization")
    # # print(des_gar1)
    # # print('\n'*5)
    # #
    # # print("This is original cesar")
    # # print(cesar_1)
    # # print()
    # # print("This is garage after deserialization")
    # # print(des_ces1)
    # #
    # # print("!!! -------------------- END OF JSON DESERIALIZATION ZONE--------------------!!!")
    # #
    #
    # # # PICKLE SERIALIZATION
    # # print("!!!--------------------PICKLE SERIALIZATION ZONE--------------------!!!")
    # # print("Car serialization:")
    # # print(pickle_serialized_car)
    # # print('\n'*5)
    # # print("Garage serialization:")
    # # print(pickle_serialized_garage)
    # # print('\n'*5)
    # # print("Cesar serialization:")
    # # print(pickle_serialized_cesar)
    # # print('\n'*5)
    # #
    # # print("!!!--------------------PICKLE DESERIALIZATION ZONE--------------------!!!")
    # # print("This is original car")
    # # print(car1)
    # # print()
    # # print("This is car after deserialization")
    # # print(des_car2)
    # # print('\n'*5)
    # #
    # # print("This is original garage")
    # # print(garage1)
    # # print()
    # # print("This is garage after deserialization")
    # # print(des_gar2)
    # # print('\n'*5)
    # #
    # # print("This is original cesar")
    # # print(cesar_1)
    # # print()
    # # print("This is garage after deserialization")
    # # print(des_ces2)
    #
    # """Для попереднього домашнього завдання.
    # Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
    # з (yaml, json, pickle) файлу відповідно
    #
    # Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
    # yaml, json, pickle відповідно."""
    #
    # # JSON SERIALIZATION
    # with open('result_car_serialization.json', 'w') as file:
    #     json.dump(car1, file, cls=JsonConverter, indent=4)
    #
    # with open('result_garage_serialization.json', 'w') as file:
    #     json.dump(garage1, file, cls=JsonConverter, indent=4)
    #
    # with open('result_cesar_serialization.json', 'w') as file:
    #     json.dump(cesar_1, file, cls=JsonConverter, indent=4)
    #
    # # JSON DESERIALIZATION
    # with open('result_car_serialization.json', 'r') as file:
    #     des_car3 = json.load(file, object_hook=json_hook)
    #
    # with open('result_garage_serialization.json', 'r') as file:
    #     des_gar3 = json.load(file, object_hook=json_hook)
    #
    # with open('result_cesar_serialization.json', 'r') as file:
    #     des_ces3 = json.load(file, object_hook=json_hook)
    #
    # # PICKLE SERIALIZATION
    # with open('pickle_result_car_serialization.txt', 'wb') as file:
    #     pickle.dump(car1, file)
    #
    # with open('pickle_result_garage_serialization.txt', 'wb') as file:
    #     pickle.dump(garage1, file)
    #
    # with open('pickle_result_cesar_serialization.txt', 'wb') as file:
    #     pickle.dump(cesar_1, file)
    #
    # # PICKLE DESERIALIZATION
    # with open('pickle_result_car_serialization.txt', 'rb') as file:
    #     des_car4 = pickle.load(file)
    #
    # with open('pickle_result_garage_serialization.txt', 'rb') as file:
    #     des_gar4 = pickle.load(file)
    #
    # with open('pickle_result_cesar_serialization.txt', 'rb') as file:
    #     des_ces4 = pickle.load(file)
    #
    # # YAML SERIALIZATION
    # yaml = YAML(typ='unsafe')
    # yaml.register_class(Car)
    # yaml.register_class(uuid.UUID)
    # yaml.register_class(Garage)
    # yaml.register_class(Cesar)
    #
    # with open('yaml_result_car_serialization.yaml', 'w') as file:
    #     yaml.dump(car1, file)
    #
    # with open('yaml_result_garage_serialization.yaml', 'w') as file:
    #     yaml.dump(garage1, file)
    #
    # with open('yaml_result_cesar_serialization.yaml', 'w') as file:
    #     yaml.dump(cesar_1, file)
    #
    # # YAML DESERIALIZATION
    #
    # with open('yaml_result_car_serialization.yaml', 'r') as file:
    #     des_car5 = yaml.load(file)
    #
    # with open('yaml_result_garage_serialization.yaml', 'r') as file:
    #     des_gar5 = yaml.load(file)
    #
    # with open('yaml_result_cesar_serialization.yaml', 'r') as file:
    #     des_ces5 = yaml.load(file)
    #
    # with open('yaml_result_cesar_serialization.yaml', 'w') as file:
    #     yaml.dump(cesar_1, file)
    #
    # # YAML DESERIALIZATION
    #
    # with open('yaml_result_car_serialization.yaml', 'r') as file:
    #     des_car5 = yaml.load(file)
    #
    # with open('yaml_result_garage_serialization.yaml', 'r') as file:
    #     des_gar5 = yaml.load(file)
    #
    # with open('yaml_result_cesar_serialization.yaml', 'r') as file:
    #     des_ces5 = yaml.load(file)
    #
    # # print("!!! --------------------JSON DESERIALIZATION ZONE--------------------!!!")
    # # print('This is the car after serailization ')
    # # print(des_car3)
    # # print()
    # #
    # # print('This is the garage after serailization ')
    # # print(des_gar3)
    # # print()
    # #
    # # print('This is cesar after serailization ')
    # # print(des_ces3)
    # # print("!!! -------------------- END OF JSON DESERIALIZATION ZONE--------------------!!!")
    #
    # # print("!!! --------------------PICKLE DESERIALIZATION ZONE--------------------!!!")
    # # print('This is the car after serailization ')
    # # print(des_car4)
    # # print()
    # #
    # # print('This is the garage after serailization ')
    # # print(des_gar4)
    # # print()
    # #
    # # print('This is cesar after serailization ')
    # # print(des_ces4)
    # # print("!!! -------------------- END OF PICKLE DESERIALIZATION ZONE--------------------!!!")
    #
    # #
    # # print("!!! --------------------YAML DESERIALIZATION ZONE--------------------!!!")
    # # print('This is the car after serailization ')
    # # print(des_car5)
    # # print()
    # #
    # # print('This is the garage after serailization ')
    # # print(des_gar5)
    # # print()
    # #
    # # print('This is cesar after serailization ')
    # # print(des_ces5)
    # # print("!!! -------------------- END OF YAML DESERIALIZATION ZONE--------------------!!!")
    #
    # # INI SERIALIZATION
    # with open('ini_car_serialization.ini', 'w') as file:
    #     params = car1.to_ini()
    #     Config = configparser.ConfigParser()
    #     Config.add_section("Car")
    #     for k, v in params.items():
    #         Config.set('Car', k, str(v))
    #     Config.write(file)
    #
    # # INI DESERIALIZATION
    # # with open('ini_car_serialization.ini') as file:
    # # params=dict()
    # # config = configparser.ConfigParser()
    # # y = config.read('ini_car_serialization.ini')
    # # config.sections()
    # # for section in config.sections():
    # #     for option in config.options(section):
    # #         # params.update({option:y[option]})
    # #         print(type(option))
    # #         print(option, config.get(section, option))
    # # print(params)
    #
    # # config = configparser.RawConfigParser(allow_no_value=True)
    # # config.readfp(io.BytesIO(car))
    #
    # # print("List all contents")
    # # for section in config.sections():
    # #     print("Section: %s" % section)
    # #     for options in config.options(section):
    # #         print("x %s:::%s:::%s" % (options,
    # #                                   config.get(section, options),
    # #                                   str(type(options))))
