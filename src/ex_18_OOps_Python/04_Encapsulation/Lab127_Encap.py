class Car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def strat_engine(self):
        print("starting a car with the name" + self.name)
        print("starting a car with the make" + self.make)
        print("starting a car with the model" + self.model)

lambo = Car("Lambo", "V6", "2023")
lambo.strat_engine()

mg_hector = Car("Hector","1.5+ Turbo","2024")
mg_hector.strat_engine()