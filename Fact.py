from utils import X, UP, DOWN, LEFT, RIGHT

class Fact():

  # ================================================================================================
  # CONSTANTS
  # ================================================================================================
  WALL = "WALL"
  DEADLY = "DEADLY"
  CAN_EXIT = "CAN_EXIT"


  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  def __init__(self, name, notOperator = False, position = None, positionVariable = None, inference = False):
    self.__name = name
    self.__not = notOperator
    self.__position = position
    self.__positionVariable = positionVariable
    self.__inference = inference


  # ================================================================================================
  # STATIC METHODS
  # ================================================================================================
  # Return True if factList contains fact, False otherwise
  @staticmethod
  def factListContains(factList, fact):
    for f in factList:
      if(f.equals(fact)):
        return True

    return False

  # Return True if fact is in contradiction with an inference fact in factList, False otherwise
  @staticmethod
  def hasContradiction(factList, fact):
    for f in factList:
      if(f.isInference() and f.contradicts(fact)):
        return True

    return False

  @staticmethod
  def addFact(fact, facts):
    for f in facts:
      if f.equals(fact):
        return
    
    facts.append(fact)

  @staticmethod
  def displayFacts(facts, end="\n"):
    print("[", end="", sep="")
    for i in range(len(facts)):
      facts[i].toString()
      if(i != len(facts) - 1): print(", ", end="")
    print("]", sep="", end=end)


  # ================================================================================================
  # PUBLIC METHODS
  # ================================================================================================
  def getName(self):
    return self.__name

  def getNot(self):
    return self.__not

  def getPosition(self):
    return self.__position

  def setPosition(self, position):
    if(self.__positionVariable != None):
      self.__position = self.__positionVariable(position)

  def resetPosition(self):
    self.__position = None

  def resetPositionVariable(self):
    self.__positionVariable = None

  def setInference(self):
    self.__inference = True

  def isInference(self):
    return self.__inference

  # 3 type of facts:
  # * normal fact: not = False, name, position
  # * not fact: not = True, name, position
  # * terminal fact: name, position = None
  def contradicts(self, fact):
    # If fact of type terminal
    if(
      self.__position == None or
      fact.__position == None
    ):
      return False

    # Else
    if(
      self.__name != fact.__name and
      self.__position == fact.__position
    ):
      return True

    return False

  def copy(self):
    return Fact(
      self.__name,
      self.__not,
      self.__position,
      self.__positionVariable
    )

  def equals(self, fact):
    if(
      self.__name == fact.__name and
      self.__position == fact.__position
    ):
      return True

    return False

  def toString(self):
    if(self.__not):
      print("not ", end="")
    if(self.__positionVariable != None):
      print(self.__name, "(", self.__position, ", ", self.__positionVariable.__name__, ")", end="", sep="")
    else:
      print(self.__name, "(", self.__position, ")", end="", sep="")
