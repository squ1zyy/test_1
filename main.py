class Car:
    def __init__(self, engine, wheels, transmission, color, motor):
        self.engine = engine
        self.wheels = wheels
        self.transmission = transmission
        self.color = color
        self.motor = motor


class McLaren(Car):
    def __init__(self, engine, wheels, transmission, color, motor):
        super(McLaren).__init__(engine, wheels, transmission, color, motor)
        self.model = "720S"
        self.r_wheels = "19"

    def start_engine(self):
        print("McLaren launched engine.")
        print("McLaren turned on the car heater.")
        print("McLaren turned on the heated seats.")
        print("McLaren turned on the relax music.")
        print("McLaren turned on hypersport mode.")


class Audi(Car):
    def __init__(self, engine, wheels, transmission, color, motor):
        super(Audi).__init__(engine, wheels, transmission, color, motor)
        self.model = "R8"
        self.r_wheels = "20"

    def start_engine(self):
        print("Audi launched engine.")
        print("Audi turned on the car heater.")
        print("Audi turned on the heated seats.")
        print("Audi turned on the relax music.")

class Jaguar(Car):
    def __init__(self, engine, wheels, transmission, color, motor):
        super(Jaguar).__init__(engine, wheels, transmission, color, motor)
        self.model = "R8"
        self.r_wheels = "20"

    def start_engine(self):
        print("Jaguar launched engine.")
        print("Jaguar turned on the car heater.")
        print("Jaguar turned on the heated seats.")
        print("Jaguar turned on the relax music.")

class Mercedes(Car):
    def __init__(self, engine, wheels, transmission, color, motor):
        super(Mercedes).__init__(engine, wheels, transmission, color, motor)
        self.model = "GLE 400d"
        self.r_wheels = "20"

    def start_engine(self):
        print("Mercedes launched engine.")
        print("Mercedes turned on the car heater.")
        print("Mercedes turned on the heated seats.")
        print("Mercedes turned on the relax music.")