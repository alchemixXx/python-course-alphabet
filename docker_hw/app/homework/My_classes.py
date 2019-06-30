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

import uuid
import random
from  constants import *
import json


class Car():

    def __init__(self, price: float, type, producer, milege: float, ):
        self.price = price
        if type in CARS_TYPES:
            self.type = type
        if producer in CARS_PRODUCER:
            self.producer = producer
        self.number = uuid.uuid4()
        self.milege = milege

    def __eq__(self, other):
        return other.price == self.price

    def __le__(self, other):
        return self.price <= other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    # def compair_cars_by_price(self, other):
    #     if self.price == other.price:
    #         return "{} and {} cars have same price".format(self.type and other.type)
    #     elif self.price > other.price:
    #         return "{} more expensive that {}".format(self.type, other.type)
    #     else:
    #         return "{} less expencive that {}".format(self.type, other.type)


    def change_number(self):
        self.number = str(uuid.uuid4())
        return "You new number is {}".format(self.number)
    def __str__(self):
        return "Car(My price: %r, my type: %r, my producer: %r, my number:%r, my milege: %r)" % (
        self.price, self.type, self.producer, self.number, self.milege)

    def __repr__(self):
        return "Car(My price: %r, my type: %r, my producer: %r, my number:%r, my milege: %r)" % (
        self.price, self.type, self.producer, self.number, self.milege)

    def convert_to_dict_car(self):
        obj_dict = {"__class__": self.__class__.__name__, "__module__": self.__module__}
        obj_dict.update(self.__dict__)
        obj_dict['number'] = str(obj_dict['number'])
        return obj_dict

    def dict_to_object_car(self,our_dict):
        if "__class__" in our_dict:
            class_name = our_dict.pop("__class__")
            module_name = our_dict.pop("__module__")
            module = __import__(module_name)
            class_ = getattr(module, class_name)
            obj = class_(**our_dict)
        else:
            obj = our_dict
        return obj

    def json_car_dumps(self):
        json_car = self.convert_to_dict_car()
        return json.dumps(json_car, indent=4)

    def json_car_dump(self):
        with open('my_json_car.txt', 'w') as file:
            json.dump(self.convert_to_dict_car(), file, indent=4)

    def json_car_loads(self, our_dict):
        return json.loads(our_dict, object_hook=my_json_car.dict_to_object_car(our_dict))

    # def json_car_load(self):



class Garage():
    def __init__(self, cars: list, town, places: int, owner=None):
        if town in TOWNS:
            self.town = town
        self.cars = cars
        self.places = places - len(cars)
        self.owner = uuid.uuid4()
        self.counter = 0

    def add(self, new_car):
        if self.places != 0:
            self.cars.append([new_car])
            self.places -= 1
            return 'Your car has been added'
        else:
            return 'No more place'

    def remove(self, remove_car):
        self.cars.remove(remove_car)
        self.places += 1
        return 'Your car was removed'

    def hit_hap(self):
        all_price = 0
        for this_car in self.cars:
            all_price += this_car.__dict__['price']
        return all_price

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.cars):
            my_car = self.cars[self.counter]
            self.counter += 1
            return my_car
        else:
            raise StopIteration

    def __str__(self):
        return "Garage(My town:%r, my cars: %r, i have %r places)" % (self.town, self.cars, self.places)

    def __repr__(self):
        return "Garage(My town:%r, my cars: %r, i have %r places)" % (self.town, self.cars, self.places)


class Collectioner():

    def __init__(self, name: str, garages=0):
        self.name = name
        self.garages = [garages]
        self.register_id = uuid.uuid4()
        self.counter = 0

    def hit_hat(self):
        price_collectioner = 0
        for a_car in self.garages:
            for this_car in a_car.__dict__['cars']:
                price_collectioner += this_car.__dict__['price']
            return price_collectioner

    def garages_count(self):
        return  len(self.garages)

    def cars_count(self):
        count = 0
        for members in self.garages:
            for some in members:
                count += 1
        return count



    def add_car(self, new_car, garage=None):
        for garage_class in self.garages:
            if garage in self.garages:
                if garage.__dict__['places'] != 0:
                    garage.__dict__['cars'] += [new_car]
                    return 'Car was added'''
                else:
                    return 'No more place in garage.Choose next one'''

            else:
                a = 0
                if a < int(garage_class.__dict__['places']):
                    a = int(garage_class.__dict__['places'])
                if a == int(garage_class.__dict__['places']) and a != 0:
                    garage_class.__dict__['cars'] += [new_car]
                    return 'Car was added'
                else:
                    return 'No more place'

    # def compare_collectioner(self, other):
    #     if self.hit_hat() > other.hit_hat():
    #         return "{} have more expencive car than {}".format(self.name, other.name)
    #     elif self.hit_hat() < other.hit_hat():
    #         return "{} have less expencive car than {}".format(self.name, other.name)
    #     else:
    #         return "{} and {} have same cars".format(self.name, other.name)
    # def __iter__(self):

    def __eq__(self, other):
        return other.hit_hat() == self.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __ge__(self, other):
        return self.hit_hat() >= other.hit_hat



    def __next__(self):
        if self.counter < len(self.garages):
            my_garages = self.garages[self.counter]
            self.counter += 1
            return my_garages
        else:
            raise StopIteration

    def __str__(self):
        return "Collectioner(My name is %r,and i have %r garagers,here my register id %r)" % (
        self.name, self.garages, self.register_id)

    def __repr__(self):
        return "Collectioner(My name is %r,and i have %r garagers,here my register id %r)" % (
        self.name, self.garages, self.register_id)


# __TEST__ME__

car_1 = Car(20000, random.choice(CARS_TYPES), random.choice(CARS_PRODUCER), 17000)
car_2 = Car(3248, random.choice(CARS_TYPES), random.choice(CARS_PRODUCER), 23443)
car_3 = Car(890, random.choice(CARS_TYPES), random.choice(CARS_PRODUCER), 23423)
car_4 = Car(9078, random.choice(CARS_TYPES), random.choice(CARS_PRODUCER), 5675)
car_5 = Car(8908, random.choice(CARS_TYPES), random.choice(CARS_PRODUCER), 89076)

garage_1 = Garage([], random.choice(TOWNS), 3)
garage_2 = Garage([car_1], random.choice(TOWNS), 7)
garage_3 = Garage([car_2, car_3], random.choice(TOWNS), 8)
garage_4 = Garage([car_3, car_4, car_5], random.choice(TOWNS), 1)

collectionar_1 = Collectioner('Jshua')
collectionar_2 = Collectioner('Myhamed')
my_json_car = car_2.json_car_dumps()
print(my_json_car)
print(type(my_json_car))

print(car_2.json_car_loads(my_json_car))

# ___CAR____

# print(car_1)
# print(car_2)
# print(car_3.change_number())
# print(car_3.compair_cars_by_price(car_4))
#
# # ___GARAGE___
#
# print(garage_1)
# print(garage_1.add(car_4))
# print(garage_3.remove(car_2))
# print(garage_2.hit_hap())
#
# # ___COLLECTIONARE___
collectionar_1.garages = [garage_1]
collectionar_2.garages = [garage_4]
# print(collectionar_1)
# print(collectionar_1.hit_hat())
# print(collectionar_2.hit_hat())
# print(collectionar_2.cars_count())
# print(collectionar_2.garages_count())
# print(collectionar_1.add_car(car_1, garage_2))
# print(collectionar_1)
# print(collectionar_1.hit_hat())
#
# print(collectionar_1.add_car(car_2, garage_1))
# print(collectionar_1)
# print(collectionar_1.hit_hat())
# print(collectionar_1.compare_collectioner(collectionar_2))