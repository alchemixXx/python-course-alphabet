import homework as hw
from constants import CARS_TYPES, CARS_PRODUCER, TOWNS
from constants import NAMES
import random

car1 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f53', car_type="Diesel", producer="Ford")
car2 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f53', car_type="Diesel", producer="Ford")
car3 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f55', car_type="Diesel", producer="Ford")  # difference in last number of uuid

car4 = hw.Car(random.randrange(100, 1000), random.randrange(100, 2000), random.choice(CARS_PRODUCER),
           random.choice(CARS_TYPES))
car5 = hw.Car(random.randrange(100, 1000), random.randrange(100, 2000), random.choice(CARS_PRODUCER),
           random.choice(CARS_TYPES))

garage1 = hw.Garage(random.randrange(5, 150), random.choice(TOWNS), car1, car2)

garage2 = hw.Garage(random.randrange(5, 150), random.choice(TOWNS), car3)

garage3 = hw.Garage(random.randrange(5, 150), random.choice(TOWNS), car4, car5)

cesar_1 = hw.Cesar(random.choice(NAMES), garage1, garage3)
cesar_2 = hw.Cesar(random.choice(NAMES), garage2)

if __name__ == '__main__':

    print(vars(car2))

    # print(car1)
    # print(car2)
    # print(car3)
    # print(car4)
    # print(car5)
    #
    # print(garage1)
    # print(garage2)
    # print(garage3)
    #
    # print(cesar_1)
    # print(cesar_2)

