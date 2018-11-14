from abc import ABC, abstractmethod
from Square import Square

class Sensor(ABC):

    def __init__(self):
        super().__init__()

    # Return True if element is detected, False otherwise
    @abstractmethod
    def detect(self, elementValue):
        pass


class PoopSensor(Sensor):

    def detect(self, elementValue):
        return(elementValue == Square.MONSTER_POOP)


class WindSensor(Sensor):

    def detect(self, elementValue):
        return(elementValue == Square.WIND)


class LightSensor(Sensor):

    def detect(self, elementValue):
        return(elementValue == Square.EXIT)
