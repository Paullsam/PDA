import os.path
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        file_name, file_type = os.path.splitext(self.photo_file_name)
        return file_type


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passengers_seats_account, car_type='car'):
        super().__init__(brand, photo_file_name, carrying)
        self.passengers_seats_account = passengers_seats_account
        self._car_type = car_type

    @property
    def car_type(self):
        return 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl=None, car_type='truck'):
        super().__init__(brand, photo_file_name, carrying)
        self._car_type = car_type
        try:
            self.body_width, self.body_height, self.body_lenght = map(float, body_whl.split('x'))
            return
        except AttributeError:
            self.body_width, self.body_height, self.body_lenght = 0, 0, 0
        except ValueError:
            self.body_width, self.body_height, self.body_lenght = 0, 0, 0
            return

    @property
    def car_type(self):
        return 'truck'

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_lenght


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra, car_type='spec_machine'):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self._car_type = car_type

    @property
    def car_type(self):
        return 'spec_machine'


def get_car_list(file_name):
    try:
        cars_in_file = []
        car_list = []
        with open(file_name) as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            next(reader)
            for row in reader:
                cars_in_file.append(row[0].split(','))
            for cars in cars_in_file:
                if cars[0] == 'car':
                    args = cars[1:]
                    car_list.append(Car(*args))
                else:
                    if cars[0] == 'truck':
                        args = cars[1:]
                        car_list.append(Truck(*args))
                    else:
                        if cars[0] == 'scec_machine':
                            args = cars[1:]
                            car_list.append(SpecMachine(*args))
    except FileNotFoundError:
        return 'File does not exist'
    return car_list


def get_car_list(file_name):
    try:
        cars_in_file = []
        car_list = []
        with open(file_name) as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            next(reader)
            for row in reader:
                cars_in_file.append(row[0].split(','))
            for cars in cars_in_file:
                if cars[0] == 'car':
                    cars.append(cars.pop(0))
                    cars = [x for x in cars if x != '']
                    car_list.append(Car(*cars))
                else:
                    if cars[0] == 'truck':
                        cars.append(cars.pop(0))
                        cars = [x for x in cars if x != '']
                        car_list.append(Truck(*cars))
                    else:
                        if cars[0] == 'spec_machine':
                            cars.append(cars.pop(0))
                            cars = [x for x in cars if x != '']
                            car_list.append(SpecMachine(*cars))
    except FileNotFoundError:
        return 'File does not exist'
    return car_list
