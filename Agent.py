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
    r = random.randint(0, 7)

    m = None
    s = None
    if(r == 0):
      m = Effector.MovementEffector.UP
    elif(r == 1):
      m = Effector.MovementEffector.DOWN
    elif(r == 2):
      m = Effector.MovementEffector.LEFT
    elif(r == 3):
      m = Effector.MovementEffector.RIGHT
    elif(r == 4):
      s = Effector.ShootingEffector.UP
    elif(r == 5):
      s = Effector.ShootingEffector.DOWN
    elif(r == 6):
      s = Effector.ShootingEffector.LEFT
    elif(r == 7):
      s = Effector.ShootingEffector.RIGHT

    if(m != None):
      error = self.__movementEffector.act(self.__forest, m)
    else:
      error = self.__shootingEffector.act(self.__forest, s)
    
    # If action has been executed
    if(error):
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
    # TODO: observe

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
