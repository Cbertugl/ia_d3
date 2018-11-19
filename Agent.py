import Effector
from Fact import Fact
from InferenceEngine import InferenceEngine
import random
from Rule import Rule
import Sensor
from Square import Square
from utils import isReachable, getMovementDirection, getShootingDirection, UP, DOWN, LEFT, RIGHT

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

    # Update knowing he just died
    if(self.__wasDead):
      fact = Fact(Fact.DEADLY, position=self.__wasDead)
      self.__wasDead = False
    # Update according to new case value
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

  def __chooseActions(self, inferenceFacts):
    playerPosition = self.__forest.getPlayerPosition()
    destination = False
    safeReachablePositions = []
    emptyPositions = []
    emptyReachablePositions = []
    monsterPositions = []
    monsterReachablePositions = []
    crevassePositions = []
    crevasseReachablePositions = []

    for fact in inferenceFacts:
      name = fact.getName()
      position = fact.getPosition()

      if(name == Fact.CAN_EXIT):
        self.__intentions.append(Effector.MovementEffector.EXIT)
        return

      if(
        isReachable(playerPosition, position) and
        name != Square.MONSTER and
        name != Square.CREVASSE and
        name != Fact.DEADLY and
        name != Fact.WALL
      ):
        safeReachablePositions.append(position)

      if(fact.isInference()):
        if(name == Square.EMPTY):
          if(isReachable(playerPosition, position)):
            emptyReachablePositions.append(position)
          else:
            emptyPositions.append(position)

        elif(name == Square.MONSTER):
          if(isReachable(playerPosition, position)):
            monsterReachablePositions.append(position)
          else:
            monsterPositions.append(position)

        elif(name == Square.CREVASSE):
          if(isReachable(playerPosition, position)):
            crevasseReachablePositions.append(position)
          else:
            crevassePositions.append(position)

    # Go to non-visited reachable empty square first
    if(len(emptyReachablePositions) > 0):
      i = random.randint(0, len(emptyReachablePositions) - 1)
      destination = emptyReachablePositions[i]

    # Then, if an empty square exists, random safe movement to get there
    elif(len(emptyPositions) > 0):
      i = random.randint(0, len(safeReachablePositions) - 1)
      destination = safeReachablePositions[i]

    # If no empty left, try to shoot a reachable monster and go there
    elif(len(monsterReachablePositions) > 0):
      i = random.randint(0, len(monsterReachablePositions) - 1)
      destination = monsterReachablePositions[i]
      self.__intentions.append(getShootingDirection(playerPosition, destination))

    # If no reachable monster, random safe movement to get there
    elif(len(monsterPositions) > 0):
      i = random.randint(0, len(safeReachablePositions) - 1)
      destination = safeReachablePositions[i]

    # If no empty square and no monster left, try every crevasse possible
    elif(len(crevasseReachablePositions) > 0):
      i = random.randint(0, len(crevasseReachablePositions) - 1)
      destination = crevasseReachablePositions[i]

    # If no reachable crevasse, random safe movement to get there
    elif(len(crevassePositions) > 0):
      i = random.randint(0, len(safeReachablePositions) - 1)
      destination = safeReachablePositions[i]

    # Otherwise, player is blocked
    else:
      print("Player is trapped forever...")

    if(destination != False):
      self.__intentions.append(getMovementDirection(playerPosition, destination))

  def __executeAction(self):
    print("Actions: ", end="")

    for action in self.__intentions:
      if(
        action == Effector.MovementEffector.EXIT or
        action == Effector.MovementEffector.UP or
        action == Effector.MovementEffector.DOWN or
        action == Effector.MovementEffector.LEFT or
        action == Effector.MovementEffector.RIGHT
      ):
        self.__movementEffector.act(self.__forest, action)
      elif(
        action == Effector.ShootingEffector.UP or
        action == Effector.ShootingEffector.DOWN or
        action == Effector.ShootingEffector.LEFT or
        action == Effector.ShootingEffector.RIGHT
      ):
        self.__shootingEffector.act(self.__forest, action)

      print(" ", end="")

    print("  ", end="")
    self.__intentions = []


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

    self.__chooseActions(inferenceFacts)

    self.__executeAction()


  # ================================================================================================
  # DISPLAY FUNCTIONS
  # ================================================================================================
  def displayBelief(self):
    print("BELIEF: ", end="")
    Fact.displayFacts(self.__belief)
