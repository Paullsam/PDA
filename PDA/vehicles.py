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
    try:
        car_list = []
        with open(file_name) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                if 'car_type' in row and row['car_type'] == 'car':
                    try:
                        if row['brand'] != '' and row['photo_file_name'] != '' and '.' in row['photo_file_name'] \
                                and int(row['passenger_seats_count']) > 0 and float(row['carrying']) > 0:
                            car_list.append(Car(row['brand'], row['photo_file_name'], float(row['carrying']),
                                                int(row['passenger_seats_count'])))
                    except (ValueError, KeyError):
                        pass
                if 'car_type' in row and row['car_type'] == 'truck':
                    try:
                        if row['brand'] != '' and row['photo_file_name'] != '' and '.' in row['photo_file_name'] \
                                and float(row['carrying']) > 0:
                            car_list.append(Truck(row['brand'], row['photo_file_name'], float(row['carrying']),
                                                  row['body_whl']))
                    except (ValueError, KeyError):
                        pass
                if 'car_type' in row and row['car_type'] == 'spec_machine':
                    try:
                        if row['brand'] != '' and row['photo_file_name'] != '' and '.' in row['photo_file_name'] \
                                and float(row['carrying']) > 0 and row['extra'] != '':
                            car_list.append(SpecMachine(row['brand'], row['photo_file_name'], float(row['carrying']),
                                                        row['extra']))
                    except (ValueError, KeyError):
                        pass
                else:
                    pass
        return car_list
    except FileNotFoundError:
        return 'File does not exist'
    return
