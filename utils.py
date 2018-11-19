from Effector import MovementEffector, ShootingEffector
import random

# ==================================================================================================
# CONSTANTS
# ==================================================================================================
BACKGROUND_COLOR = "chartreuse4"


# ==================================================================================================
# FUNCTIONS
# ==================================================================================================
def getRandomPosition(size):
  return (random.randint(0, size - 1), random.randint(0, size - 1))

# Given a chance in %, return True if you win and False otherwise
def rollDice(chance):
  r = random.uniform(0, 100)

  if(r < chance):
    return True
  else:
    return False

def getShootingDirection(myPosition, position):
  if(position == UP(myPosition)):
    return ShootingEffector.UP

  elif(position == DOWN(myPosition)):
    return ShootingEffector.DOWN

  elif(position == LEFT(myPosition)):
    return ShootingEffector.LEFT

  elif(position == RIGHT(myPosition)):
    return ShootingEffector.RIGHT
  
  return False

def getMovementDirection(myPosition, position):
  if(position == UP(myPosition)):
    return MovementEffector.UP

  elif(position == DOWN(myPosition)):
    return MovementEffector.DOWN

  elif(position == LEFT(myPosition)):
    return MovementEffector.LEFT

  elif(position == RIGHT(myPosition)):
    return MovementEffector.RIGHT
  
  return False

def isReachable(myPosition, position):
  return(getMovementDirection(myPosition, position) != False)

def X(position):
  return position
  
def UP(position):
  (l, c) = position
  return (l - 1, c)

def DOWN(position):
  (l, c) = position
  return (l + 1, c)

def LEFT(position):
  (l, c) = position
  return (l, c - 1)

def RIGHT(position):
  (l, c) = position
  return (l, c + 1)