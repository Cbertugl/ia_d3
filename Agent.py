import Effector
from Fact import Fact
from InferenceEngine import InferenceEngine
import random
import Sensor
from Square import Square
from Rule import Rule

class Agent:

  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  def __init__(self):
    # Player
    self.__wasDead = False

    # Sensors
    self.__poopSensor = Sensor.PoopSensor()
    self.__windSensor = Sensor.WindSensor()
    self.__lightSensor = Sensor.LightSensor()

    # Effectors
    self.__movementEffector = Effector.MovementEffector()
    self.__shootingEffector = Effector.ShootingEffector()

    # Environment
    self.__forest = None

    # Inference engine
    self.__inferenceEngine = InferenceEngine()

    # BDI
    self.__belief = [] # Fact array
    self.__desires = [] # Fact array
    self.__intentions = [] # Fact array


  # ================================================================================================
  # PRIVATE FUNCTIONS
  # ================================================================================================
  def __initBelief(self, forestSize):
    self.__belief = []

    for i in range(forestSize):
      self.__addBelief(Fact(Fact.WALL, position=(-1, i)))
      self.__addBelief(Fact(Fact.WALL, position=(forestSize, i)))
      self.__addBelief(Fact(Fact.WALL, position=(i, -1)))
      self.__addBelief(Fact(Fact.WALL, position=(i, forestSize)))

  def __addBelief(self, fact):
    Fact.addFact(fact, self.__belief)

  def __observe(self):
    position = self.__forest.getPlayerPosition()

    if(self.__wasDead):
      # update knowing he just died
      fact = Fact(Fact.DEADLY, position=self.__wasDead)
      self.__wasDead = False
    else:
      if(self.__poopSensor.detect(self.__forest)):
        fact = Fact(Square.MONSTER_POOP, position=position)
      elif(self.__windSensor.detect(self.__forest)):
        fact = Fact(Square.WIND, position=position)
      elif(self.__lightSensor.detect(self.__forest)):
        fact = Fact(Square.EXIT, position=position)
      else:
        fact = Fact(Square.EMPTY, position=position)

    self.__addBelief(fact)

  def __executeAction(self, inferenceFacts):
    for fact in inferenceFacts:
      if(fact.getName() == Fact.CAN_EXIT):
        self.__movementEffector.act(self.__forest, Effector.MovementEffector.EXIT)

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
      self.__movementEffector.act(self.__forest, m)
    else:
      self.__shootingEffector.act(self.__forest, s)

  
  # ================================================================================================
  # PUBLIC FUNCTIONS
  # ================================================================================================
  def setEnvironment(self, forest):
    self.__initBelief(forest.getSize())
    self.__intentions = []
    self.__forest = forest

  def setWasDead(self, position):
    self.__intentions = []
    self.__wasDead = position

  def act(self):
    self.__observe()

    inferenceFacts = self.__inferenceEngine.run(self.__belief)

    Fact.displayFacts(inferenceFacts)

    self.__executeAction(inferenceFacts)


  # ================================================================================================
  # DISPLAY FUNCTIONS
  # ================================================================================================
  def displayBelief(self):
    print("BELIEF: ", end="")
    Fact.displayFacts(self.__belief)
