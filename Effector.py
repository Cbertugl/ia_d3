from abc import ABC, abstractmethod

class Effector(ABC):

  def __init__(self):
    super().__init__()
  
  # Return True if success, False otherwise
  @abstractmethod
  def act(self):
    pass


class MovementEffector(Effector):

  UP = 1
  DOWN = 2
  LEFT = 3
  RIGHT = 4
  EXIT = 5

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

    return r


class ShootingEffector(Effector):

  UP = 6
  DOWN = 7
  LEFT = 8
  RIGHT = 9

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
