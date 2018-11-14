from abc import ABC, abstractmethod

class Effector(ABC):

    def __init__(self):
        super().__init__()
    
    # Return True if success, False otherwise
    @abstractmethod
    def act(self):
        pass


class MovementEffector(Effector):

    def act(self):
      # TODO:
      return True


class ShootingEffector(Effector):

    def act(self):
      # TODO:
      return True
