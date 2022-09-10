class Car:
    def __init__(self, engine):
        self.engine = engine


class McLaren(self):
    def __init__(self, engine):
        super(Audi).__init__(engine)
        self.model = "720S"

    def start_engine(self):
        print("McLaren launched engine.")


class Audi(self):
    def __init__(self, engine):
        super(Audi).__init__(engine)
        self.config = "R8"

    def start_engine(self):
        print("Audi launched engine.")