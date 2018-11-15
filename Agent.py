import Effector
import random
import Sensor
from Facts import Facts
from Facts import SeSituer
from Rules import Rules

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

    # Facts and Rules
    self.__facts = Facts()
    self.__rules = Rules()


  # ================================================================================================
  # PRIVATE FUNCTIONS
  # ================================================================================================
  # TODO:
  def __setFacts(self,fact):

    if fact == "poop" or fact == "wind" : 
      newFactPoopOrWind = SeSituer(fact,self.__forest.getPlayerPosition())
      if not ( self.__facts.findAFact(newFactPoopOrWind)):
        self.__facts.addAFact(newFactPoopOrWind)
    if fact == "player" :
      newFactPlayer = SeSituer(fact,self.__forest.getPlayerPosition())
      formerFactPlayer = self.__facts.findAFact(newFactPlayer)
      self.__facts.removeAFact(formerFactPlayer)
      self.__facts.addAFact(newFactPlayer)


  # TODO:
  def __getActivableRules(self):
    pass

  # TODO:
  def __chooseBestRule(self, rules):
    pass

  # TODO:
  def __executeRule(self, rule):
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
      isPoop = self.__poopSensor.detect(self.__forest)
      isWind = self.__windSensor.detect(self.__forest)
      isLight = self.__lightSensor.detect(self.__forest)
      if isPoop : self.__setFacts("poop")
      if isWind : self.__setFacts("wind")
      self.__setFacts("player")
      print(self.__facts.getFacts())
    # If there has been an error in the action
    else:
      # TODO: handle it
      pass

  def __inferenceEngine(self):
    activableRules = self.__getActivableRules()

    bestRule = self.__chooseBestRule(activableRules)

    self.__executeRule(bestRule)

  
  # ================================================================================================
  # PUBLIC FUNCTIONS
  # ================================================================================================
  def setEnvironment(self, forest):
    self.__forest = forest

  def nextAction(self):
    self.__inferenceEngine()
