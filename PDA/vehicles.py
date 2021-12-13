import os.path
import csv

class CarBase:
    def __init__(self, car_type, photo_file_name, brand, carrying):
        self.car_type = car_type
        self.get_photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self, path):
        file_name, file_type = os.path.splitext(self.path)
        return file_type

class Car(CarBase):
    def __init__(self, car_type, photo_file_name, brand, passengers_seats_count):
        pass

class Truck(CarBase):
    def __init__(self, car_type, photo_file_name, brand, body_whl=None):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.body_whl = body_whl
        try:
           body_width, body_height, body_lenght = map(float, body_whl.split('x'))
           return
        except AttributeError:
            body_width, body_height, body_lenght = 0
            return

    def get_body_volume(self):
        self.body_width * self.body_height * self.body_lenght



class SpecMachine(CarBase):
    def __init__(self, car_type, photo_file_name, brand, ):
        pass
