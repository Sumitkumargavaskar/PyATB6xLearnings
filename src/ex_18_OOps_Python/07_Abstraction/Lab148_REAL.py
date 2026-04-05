from abc import ABC, abstractmethod

class GearBox(ABC):
    @abstractmethod
    def start(self):
        pass

class Engine:
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class car(Engine,GearBox):
    def start(self):
        print("Starting")

    def stop(self):
        print("Stopping")

    def setGear(self):
        print("Gearbox is ready")

    def driver(self):
        self.start()
        self.setGear()
        self.stop()

tesla = car()
tesla.driver()