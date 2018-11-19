from abc import ABC, abstractmethod

class Effector(ABC):

  def __init__(self):
    super().__init__()
  
  # Return True if success, False otherwise
  @abstractmethod
  def act(self):
    pass


class MovementEffector(Effector):

  UP = "MOVE_UP"
  DOWN = "MOVE_DOWN"
  LEFT = "MOVE_LEFT"
  RIGHT = "MOVE_RIGHT"
  EXIT = "MOVE_EXIT"

  def act(self, environment, action):
    print(action, end="")

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

  UP = "SHOOT_UP"
  DOWN = "SHOOT_DOWN"
  LEFT = "SHOOT_LEFT"
  RIGHT = "SHOOT_RIGHT"

  def act(self, environment, action):
    print(action, end="")

    if(action == self.UP):
      r = environment.playerShootUp()
    elif(action == self.DOWN):
      r = environment.playerShootDown()
    elif(action == self.LEFT):
      r = environment.playerShootLeft()
    elif(action == self.RIGHT):
      r = environment.playerShootRight()
    
    return r
