class Car:
    def __init__(self, brand, car_type, name, price):
        self.brand = brand
        self.car_type = car_type
        self.name = name
        self.price = price

    def show(self):
        print("\nModel: ", self.name)
        print("Type: ", self.car_type)
        print("Price: RM", self.price)


class Axia(Car):
    def __init__(self,  brand, car_type, name, price, type, Transmission, Fuel_C, Audio, Seat_S, Rear_S):
        Car.__init__(self, brand, car_type, name, price)
        self.type= type
        self.Transmission= Transmission
        self.Fuel_C= Fuel_C
        self.Audio= Audio
        self.Sear_S= Seat_S
        self.Rear_S= Rear_S

    def show(self):
        print("\nModel: ", self.name)
        print("Type: ", self.car_type)
        print("Price: RM", self.price)
        print("Type: ", self.type)
        print("Transmission: ", self.Transmission)
        print("Fuel Consumption: ", self.Fuel_C)
        print("Audio: ", self.Audio)
        print("Seat Material: ", self.Sear_S)
        print("Rear Sensor: ", self.Rear_S)


class Bezza(Car):
    def __init__(self,  brand, car_type, name, price, type, engine_S, Transmission, Fuel_C, Audio, Seat_S, Rear_H):
        Car.__init__(self, brand, car_type, name, price)
        self.type= type
        self.engine_S= engine_S
        self.Transmission= Transmission
        self.Fuel_C= Fuel_C
        self.Audio= Audio
        self.Sear_S= Seat_S
        self.Rear_H= Rear_H

    def show(self):
        print("\nModel: ", self.name)
        print("Type: ", self.car_type)
        print("Price: RM", self.price)
        print("Type: ", self.type)
        print("Engine Size: ", self.engine_S)
        print("Transmission: ", self.Transmission)
        print("Fuel Consumption: ", self.Fuel_C)
        print("Audio: ", self.Audio)
        print("Seat Material: ", self.Sear_S)
        print("Rear Headphone Slot: ", self.Rear_H)


class Alza(Car):
    def __init__(self, brand, car_type, name, price, type, Transmission, Audio, Seat_S, Shoppin_H):
        Car.__init__(self, brand, car_type, name, price)
        self.type = type
        self.Transmission = Transmission
        self.Audio = Audio
        self.Seat_S = Seat_S
        self.Shoppin_H = Shoppin_H

    def show(self):
        print("\nModel: ", self.name)
        print("Type: ", self.car_type)
        print("Price: RM", self.price)
        print("Type: ", self.type)
        print("Transmission: ", self.Transmission)
        print("Audio: ", self.Audio)
        print("Seat Material: ", self.Seat_S)
        print("Shopping Hook: ", self.Shoppin_H)


class MyVi(Car):
    def __init__(self, brand, car_type, name, price, type, Engine_S, Transmission, Fuel_C, Audio, Eco_I, Reverse_C):
        Car.__init__(self, brand, car_type, name, price)
        self.type = type
        self.Engine_S= Engine_S
        self.Transmission = Transmission
        self.Fuel_C = Fuel_C
        self.Audio = Audio
        self.Eco_I = Eco_I
        self.Reverse_C = Reverse_C

    def show(self):
        print("\nModel: ", self.name)
        print("Type: ", self.car_type)
        print("Price: RM", self.price)
        print("Type: ", self.type)
        print("Engine size: ", self.Engine_S)
        print("Transmission: ", self.Transmission)
        print("Fuel Consumption: ", self.Fuel_C)
        print("Audio: ", self.Audio)
        print("Eco Idle: ", self.Eco_I)
        print("Reverse Camera: ", self.Reverse_C)