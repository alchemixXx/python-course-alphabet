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

    def __init__(self, price: float, mileage: float, producer, type, garage_numb=None):
        self.price = float(price)
        self.number = uuid.uuid4()
        self.mileage = float(mileage)
        self.garage_numb = garage_numb
        self.producer = self.producer_checking(producer)
        self.car_type = self.type_checking(type)

    def __repr__(self):
        return f'Car(float(price)="{self.price}", self.type_checking(type)="{self.car_type}", uuid.uuid4()="{self.number}",' \
            f'float(mileage)="{self.mileage}", self.producer_checking(producer)="{self.producer}", garage_numb="{self.garage_numb}")'

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

    def change_number(self, new_number):
        if re.search('[\w]{8}-[\w]{4}-4[\w]{3}-[\w][\w]{3}-[\w]{12}', new_number):
            self.number = new_number
        else:
            print('Sorry, you have entered wrong number')
            # raise ValueError


class Garage:
    cars = List[Car]
    garage_number = itertools.count()

    @staticmethod
    def owner_checking(owner):
        if re.search('[\w]{8}-[\w]{4}-4[\w]{3}-[\w][\w]{3}-[\w]{12}', owner):
            return owner
        else:
            print("Owner should be UUID!")
            # return None

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
        return actual_cars

    def __init__(self, places: int, town, *cars, owner=None):
        self.places = int(places)
        self.owner = self.owner_checking(owner)
        self.number = next(Garage.garage_number)
        self.cars = self.cars_checking(cars)
        self.town = self.town_checking(town)

    def all_cars(self):
        return [car for car in self.cars]

    def add(self, car):
        if len(self.cars) < self.places:
            if car.garage_numb == None:
                car.garage_numb = self.garage_number
                return self.cars.append(car)
            else:
                print("This car is already in other garage")
        else:
            print("Sorry, this garage is full. Car has not been changed")
            # raise ValueError

    def remove(self, car):
        if car in self.cars:
            return self.cars.remove(car)
        else:
            print("Sorry, there is no that car in the garage")
            # raise ValueError

    def hit_hat(self):
        return sum([car.price for car in self.cars])

    def __str__(self):
        return f"""This garage has next attributes:
        cars =  '{len(self.cars)} cars', 
        owner = '{self.owner}',
        town = '{self.town}',
        number = '{self.number}'
        """

    def __repr__(self):
        return f'Garage(int(places)="{self.places}", self.owner_checking(owner)="{self.owner}", ' \
            f'number="{next(Garage.garage_number)}",' \
            f'self.cars_checking(cars)="{self.cars}", self.town_checking(town)="{self.town}")'

    def change_owner(self, owner_id):
        if re.search('[\w]{8}-[\w]{4}-4[\w]{3}-[\w][\w]{3}-[\w]{12}', owner_id):
            self.owner = owner_id
        else:
            print("Sorry, it's not UUID. Owner has not been changed")
            # raise ValueError


class Cesar:
    garages = List[Garage]

    @staticmethod
    def garages_checking(garages):
        if len(garages) > 0:
            return garages
        else:
            return []

    def __init__(self, name, *garages):
        self.name = name
        self.register_id = uuid.uuid4()
        self.garages = self.garages_checking(garages)

    def garages_count(self):
        return len(self.garages)

    def __str__(self):
        return (f"""This Cesar has next attributes:
        name = '{self.name}',
        id = '{self.register_id}',
        number of garages = {self.garages_count()}""")

    def __repr__(self):
        return f'Cesar(name="{self.name}", uuid.uuid4()="{self.register_id}", ' \
            f'self.garages_checking(garages)="{self.garages}")'

    def hit_hat(self):
        return sum([sum([car.price for car in garage.cars]) for garage in self.garages])
        # total_price = 0
        # for garage in self.garages:
        #     for car in garage.cars:
        #         total_price += car.price
        # return total_price

    def cars_count(self):
        return sum([len(garage.cars) for garage in self.garages])

    def add_car(self, car, chosen_garage = None):
        if chosen_garage == None:
            def max_free():
                all_garages = {garage.number: (garage.places - len(garage.cars)) for garage in self.garages}
                max_free_garage = {key:value for (key,value) in all_garages.items() if value == max(all_garages.values())}

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
        else:
            if (chosen_garage.places - len(chosen_garage.cars)) != 0:
                chosen_garage.add(car)
                return f"Car has been added to garage {chosen_garage}"
            else:
                return f"Sorry, there is no free places in the garage {chosen_garage}"

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

    garage1 = Garage(random.randrange(5, 150), random.choice(TOWNS), car1, car2,
                     owner=str(uuid.uuid4()))


    garage2 = Garage(random.randrange(5, 150), random.choice(TOWNS), car3,
                     owner=random.choice(NAMES))

    garage3 = Garage(random.randrange(5, 150), random.choice(TOWNS), car4, car5,
                     owner=random.choice(NAMES))

    garage4 = Garage(random.randrange(5, 150), random.choice(TOWNS), car6, car7,
                     owner=random.choice(NAMES))

    garage5 = Garage(random.randrange(5, 150), random.choice(TOWNS), car8, car9,
                     owner=random.choice(NAMES))

    print(garage1, garage2, garage3, garage4, garage5)
    print(garage1, garage2)
    print(uuid.uuid4())
    print(garage1.hit_hat())

    cesar_1 = Cesar(random.choice(NAMES), garage1, garage3)
    cesar_2 = Cesar(random.choice(NAMES), garage2)
    cesar_3 = Cesar(random.choice(NAMES), garage4, garage5)
    print(cesar_1)
    print(cesar_2)
    print(cesar_3)

    print(garage1.all_cars())
    print(garage2.all_cars())

    print(cesar_1.hit_hat())
    print(cesar_1.cars_count())

    print(cesar_1.add_car(car10))
