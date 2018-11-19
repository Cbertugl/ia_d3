import Effector
from Fact import Fact
import random
import Sensor
from Square import Square
from Rule import Rule
from utils import X, UP, DOWN, LEFT, RIGHT

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

    # BDI
    self.__belief = [] # Fact array
    self.__desires = [] # Fact array
    self.__intentions = [] # Fact array

    # Rules
    self.__rules = []
    self.__initRules()


  # ================================================================================================
  # PRIVATE FUNCTIONS
  # ================================================================================================
  def __initRules(self):
    self.__rules = [
      # EMPTY => EMPTY
      Rule(
        [
          Fact(Square.EMPTY, positionVariable=X),
          Fact(Fact.WALL, positionVariable=UP, notOperator=True)
        ],
        [ Fact(Square.EMPTY, positionVariable=UP) ]
      ),
      Rule(
        [
          Fact(Square.EMPTY, positionVariable=X),
          Fact(Fact.WALL, positionVariable=DOWN, notOperator=True)
        ],
        [ Fact(Square.EMPTY, positionVariable=DOWN) ]
      ),
      Rule(
        [
          Fact(Square.EMPTY, positionVariable=X),
          Fact(Fact.WALL, positionVariable=LEFT, notOperator=True)
        ],
        [ Fact(Square.EMPTY, positionVariable=LEFT) ]
      ),
      Rule(
        [
          Fact(Square.EMPTY, positionVariable=X),
          Fact(Fact.WALL, positionVariable=RIGHT, notOperator=True)
        ],
        [ Fact(Square.EMPTY, positionVariable=RIGHT) ]
      ),

      # MONSTER_POOP => MONSTER
      Rule(
        [
          Fact(Square.MONSTER_POOP, positionVariable=X),
          Fact(Fact.WALL, positionVariable=UP, notOperator=True)
        ],
        [ Fact(Square.MONSTER, positionVariable=UP) ]
      ),
      Rule(
        [
          Fact(Square.MONSTER_POOP, positionVariable=X),
          Fact(Fact.WALL, positionVariable=DOWN, notOperator=True)
        ],
        [ Fact(Square.MONSTER, positionVariable=DOWN) ]
      ),
      Rule(
        [
          Fact(Square.MONSTER_POOP, positionVariable=X),
          Fact(Fact.WALL, positionVariable=LEFT, notOperator=True)
        ],
        [ Fact(Square.MONSTER, positionVariable=LEFT) ]
      ),
      Rule(
        [
          Fact(Square.MONSTER_POOP, positionVariable=X),
          Fact(Fact.WALL, positionVariable=RIGHT, notOperator=True)
        ],
        [ Fact(Square.MONSTER, positionVariable=RIGHT) ]
      ),

      # WIND => CREVASSE
      Rule(
        [
          Fact(Square.WIND, positionVariable=X),
          Fact(Fact.WALL, positionVariable=UP, notOperator=True)
        ],
        [ Fact(Square.CREVASSE, positionVariable=UP) ]
      ),
      Rule(
        [
          Fact(Square.WIND, positionVariable=X),
          Fact(Fact.WALL, positionVariable=DOWN, notOperator=True)
        ],
        [ Fact(Square.CREVASSE, positionVariable=DOWN) ]
      ),
      Rule(
        [
          Fact(Square.WIND, positionVariable=X),
          Fact(Fact.WALL, positionVariable=LEFT, notOperator=True)
        ],
        [ Fact(Square.CREVASSE, positionVariable=LEFT) ]
      ),
      Rule(
        [
          Fact(Square.WIND, positionVariable=X),
          Fact(Fact.WALL, positionVariable=RIGHT, notOperator=True)
        ],
        [ Fact(Square.CREVASSE, positionVariable=RIGHT) ]
      ),

      # EXIT => CAN_EXIT
      Rule(
        [ Fact(Square.EXIT, positionVariable=X) ],
        [ Fact(Fact.CAN_EXIT) ],
        100
      )
    ]

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

  def __run(self, facts):
    # Init
    over = False
    inferenceFacts = facts.copy()
    for r in self.__rules:
      r.unmark()

    while(not over):
      over = True

      # Select applicable rules (not marked, no contradiction and possible)
      applicableRules = []

      for r in self.__rules:
        if(
          not r.isMarked() and
          r.isPossible(inferenceFacts)
        ):
          if(r.hasContradiction(inferenceFacts)):
            r.mark()
          else:
            applicableRules.append(r)

      # Choose which rule we apply according to priority or randomly if we
      # they all have the same priority
      if(len(applicableRules) > 0):
        over = False
        maxPriority = 0
        bestRule = None

        for r in applicableRules:
          if(r.getPriority() > maxPriority):
            maxPriority = r.getPriority()
            bestRule = r

        if(bestRule == None):
          bestRule = applicableRules[random.randint(0, len(applicableRules) - 1)]

        # Apply rule
        for f in bestRule.getConclusion(inferenceFacts):
          Fact.addFact(f, inferenceFacts)

        bestRule.mark()

    return inferenceFacts

  # TODO:
  def __executeAction(self, inferenceFacts):
    if(self.__lightSensor.detect(self.__forest)):
      self.__movementEffector.act(self.__forest, Effector.MovementEffector.EXIT)
      return

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

  def __inferenceEngine(self):
    self.__observe()

    inferenceFacts = self.__run(self.__belief)

    Fact.displayFacts(inferenceFacts)

    self.__executeAction(inferenceFacts)

  
  # ================================================================================================
  # PUBLIC FUNCTIONS
  # ================================================================================================
  def setEnvironment(self, forest):
    self.__initBelief(forest.getSize())
    self.__intentions = []
    self.__forest = forest

  def nextAction(self):
    self.__inferenceEngine()

  def setWasDead(self, position):
    self.__intentions = []
    self.__wasDead = position


  # ================================================================================================
  # DISPLAY FUNCTIONS
  # ================================================================================================
  def displayBelief(self):
    print("BELIEF: ", end="")
    Fact.displayFacts(self.__belief)
