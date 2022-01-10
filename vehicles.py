import os.path
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        file_name, file_type = os.path.splitext(self.photo_file_name)
        return file_type


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count, car_type='car'):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self._car_type = car_type

    @property
    def car_type(self):
        return 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl=None, car_type='truck',
                 body_length=None, body_width=None, body_height=None):
        super().__init__(brand, photo_file_name, carrying)
        self._car_type = car_type
        try:
            self.body_length, self.body_width, self.body_height = map(float, body_whl.split('x'))
            return
        except AttributeError:
            self.body_length, self.body_width, self.body_height = float(0), float(0), float(0)
        except ValueError:
            self.body_length, self.body_width, self.body_height = float(0), float(0), float(0)
            return

    @property
    def car_type(self):
        return 'truck'

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra, car_type='spec_machine'):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self._car_type = car_type

    @property
    def car_type(self):
        return 'spec_machine'


def get_car_list(file_name):
    car_list = []
    if os.path.exists(file_name):
        with open(file_name) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                if row_validation(row):
                    if car_validation(row):
                        car_list.append(Car(row['brand'], row['photo_file_name'], float(row['carrying']),
                                            int(row['passenger_seats_count'])))
                    if truck_validation(row):
                        car_list.append(Truck(row['brand'], row['photo_file_name'], float(row['carrying']),
                                              row['body_whl']))
                    if spec_machine_validation(row):
                        car_list.append(SpecMachine(row['brand'], row['photo_file_name'], float(row['carrying']),
                                                    row['extra']))
            return car_list
    else:
        return 'File does not exist'


def row_validation(row):
    try:
        if 'car_type' in row and row['brand'].replace(' ', '') != '' \
                and ext_validation(row['photo_file_name']) and float(row['carrying']) > 0:
            return True
        else:
            return False
    except (ValueError, KeyError, TypeError):
        return False


def car_validation(row):
    try:
        if row['car_type'] == 'car' and int(row['passenger_seats_count']) > 0:
            return True
        else:
            return False
    except (ValueError, KeyError):
        pass


def truck_validation(row):
    if row['car_type'] == 'truck':
        return True
    else:
        return False


def spec_machine_validation(row):
    if row['car_type'] == 'spec_machine' and row['extra'].replace(' ', '') != '':
        return True
    else:
        return False


def ext_validation(file_name):
    if '.jpg' in file_name or '.jpeg' in file_name or '.png' in file_name or '.gif' in file_name:
        return True
    else:
        return False
