from abc import ABC, abstractmethod


class Facts:

  SAFE_UP = 0
  SAFE_DOWN = 1
  SAFE_LEFT = 2
  SAFE_RIGHT = 3

  NOT_SAFE_UP = 4
  NOT_SAFE_DOWN = 5
  NOT_SAFE_LEFT = 6
  NOT_SAFE_RIGHT = 7

  WALL_UP = 8
  WALL_DOWN = 9
  WALL_LEFT = 10
  WALL_RIGHT = 11

  POOP = 12
  WIND = 13
  LIGHT = 14

  MONSTER = 15
  CREVACE = 16



  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  def __init__(self, size):

    self.__size = size
    self.__facts = [[ Fact() for i in range(self.__size) ] for j in range(self.__size)]
    self.initialisationFacts()

  def initialisationFacts(self):
    for i in range(self.__size):
      self.__facts[0][i].addFact(self.WALL_UP)
      self.__facts[i][0].addFact(self.WALL_LEFT)
      self.__facts[self.__size - 1][i].addFact(self.WALL_DOWN)
      self.__facts[i][self.__size - 1].addFact(self.WALL_RIGHT)
    for i in range(self.__size):
      for j in range(self.__size):
        self.__facts[i][j].addFact(self.SAFE_UP)
        self.__facts[i][j].addFact(self.SAFE_DOWN)
        self.__facts[i][j].addFact(self.SAFE_LEFT)
        self.__facts[i][j].addFact(self.SAFE_RIGHT)
    




  # ================================================================================================
  # PUBLIC METHODS
  # ================================================================================================

  def getFactsArray(self):
    return self.__facts


class Fact:


  def __init__(self):
    self.__facts = []

  def addFact(self, fact):
    if not fact in self.__facts : self.__facts.append(fact)
    else : return False

  def removeFact(self,fact):
    if fact in self.__facts : self.__facts.remove(fact)

  def getFacts(self):
    return self.__facts
  
  def areFactsEqual(self,fact1,fact2):
    if fact1 == fact2 :
      return True
    return False
 