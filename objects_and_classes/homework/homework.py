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
import random
import uuid
import re
from typing import List


# a = uuid.uuid4()

class Car:
    def __init__(self, price: float, mileage: float, producer, type):
        self.price = float(price)
        self.number = uuid.uuid4()
        self.mileage = float(mileage)
        if producer in CARS_PRODUCER:
            self.producer = producer

            # self.members = members if members is not None else []
        else:
            raise ValueError
        # self.type = type if type in CARS_TYPES else ValueError
        if type in CARS_TYPES:
            self.type = type
        else:
            raise ValueError

    # return f"Programmer(name='{self.name}')"
    def __repr__(self):
        return f'Car(price="{self.price}", type="{self.type}", number="{self.number}",' \
            f'mileage="{self.mileage}", producer="{self.producer}")'

    def __str__(self):
        return f"""
        'This car has next attributes:
        price="{self.price}",
        type="{self.type}",
        number="{self.number}",
        mileage="{self.mileage}"'
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

    def change_number(self, new_number):
        # y = '[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}'
        y = '[\w]{8}-[\w]{4}-4[\w]{3}-[\w][\w]{3}-[\w]{12}'
        if re.search(y, new_number):
            self.number = new_number
        else:
            print('Sorry, you have enter wrong number')
            raise ValueError


class Garage:
    cars: List[Car]

    def __init__(self, places: int, town, owner=None, *cars):
        self.places = int(places)
        self.owner = owner
        self.cars =  cars if cars is not None else []
        if town in TOWNS:
            self.town = town
        else:
            raise ValueError

    def add(self, car):
        if len(self.cars) < self.places:
            return self.cars.append(car)
        else:
            print("Sorry, this garage is full.")
            raise ValueError

    def remove(self, car):
        if car in self.cars:
            return self.cars.remove(car)
        else:
            print("Sorry, there is no those car in the garage")
            raise ValueError

    def hit_hat(self):
        summ = 0
        return [summ + car.price for car in self.cars][0]

    def __str__(self):
        sum = 0
        for _ in self.cars:
            sum += 1
        return f"""This garage has next attributes:
        cars =  '{sum} cars', 
        owner = '{self.owner}',
        town = '{self.town}'
        """



class Cesar:
    garages = List[Garage]

    def __init__(self, name, garages=0):
        self.name = name
        self.register_id = uuid.uuid4()
        self.garages = garages if garages is not None else []


if __name__ == '__main__':
    car1 = Car(128.78, 155, "Ford", "Diesel")
    car2 = Car(158, 125, 'BMW', 'Sports Car')
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
    # print(car7)

    garage1 = Garage(random.randrange(5, 150), random.choice(TOWNS), 'Pavel', *(car1, car2, car3, car5,))
    print(garage1)





