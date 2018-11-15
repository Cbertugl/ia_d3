from abc import ABC, abstractmethod

class Effector(ABC):

  def __init__(self):
    super().__init__()
  
  # Return True if success, False otherwise
  @abstractmethod
  def act(self):
    pass


class MovementEffector(Effector):

  UP = 0
  DOWN = 1
  LEFT = 2
  RIGHT = 3
  EXIT = 4

  def act(self, environment, action):
    if(action == self.UP):
      r = environment.playerMoveUp()
    elif(action == self.DOWN):
      r = environment.playerMoveDown()
    elif(action == self.LEFT):
      r = environment.playerMoveLeft()
    elif(action == self.RIGHT):
      r = environment.playerMoveRight()
    elif(action == self.EXIT):
      r = environment.playerMoveExit()
      pass

    return r


class ShootingEffector(Effector):

  UP = 0
  DOWN = 1
  LEFT = 2
  RIGHT = 3

  def act(self, environment, action):
    if(action == self.UP):
      r = environment.playerShootUp()
    elif(action == self.DOWN):
      r = environment.playerShootDown()
    elif(action == self.LEFT):
      r = environment.playerShootLeft()
    elif(action == self.RIGHT):
      r = environment.playerShootRight()
    
    return r
