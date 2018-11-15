import Effector
import random
import Sensor

class Agent:

  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  def __init__(self):
    # Sensors
    self.__poopSensor = Sensor.PoopSensor()
    self.__windSensor = Sensor.WindSensor()
    self.__lightSensor = Sensor.LightSensor()

    # Effectors
    self.__movementEffector = Effector.MovementEffector()
    self.__shootingEffector = Effector.ShootingEffector()

    # Environment
    self.__forest = None


  # ================================================================================================
  # PRIVATE FUNCTIONS
  # ================================================================================================
  def __inferenceEngine(self):
    r = random.randint(0, 3)

    if(r == 0):
      v = Effector.MovementEffector.UP
    elif(r == 1):
      v = Effector.MovementEffector.DOWN
    elif(r == 2):
      v = Effector.MovementEffector.LEFT
    elif(r == 3):
      v = Effector.MovementEffector.RIGHT

    # If action has been executed
    if(self.__movementEffector.act(self.__forest, v)):
      print("POOP:", self.__poopSensor.detect(self.__forest))
      print("WIND:", self.__windSensor.detect(self.__forest))
      print("LIGHT:", self.__lightSensor.detect(self.__forest))
    # If there has been an error in the action
    else:
      # TODO: handle it
      pass


  
  # ================================================================================================
  # PUBLIC FUNCTIONS
  # ================================================================================================
  def setEnvironment(self, forest):
    self.__forest = forest

  def nextAction(self):
    self.__inferenceEngine()
