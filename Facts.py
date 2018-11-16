from abc import ABC, abstractmethod


class Facts:

  EMPTY = 0
  EMPTY_BELIEF = 1
  POOP = 2
  WIND = 3
  CREVACE = 4
  MONSTER = 5

  CASE_R_EMPTY = 6
  CASE_L_EMPTY = 7
  CASE_D_EMPTY = 8
  CASE_U_EMPTY = 9

  CASE_R_EMPTY_BELIEF = 10 
  CASE_L_EMPTY_BELIEF = 11 
  CASE_D_EMPTY_BELIEF = 12 
  CASE_U_EMPTY_BELIEF = 13  

  CASE_R_EMPTY_POOP = 14
  CASE_L_EMPTY_POOP = 15
  CASE_D_EMPTY_POOP = 16 
  CASE_U_EMPTY_POOP = 17

  CASE_R_EMPTY_WIND = 18
  CASE_L_EMPTY_WIND = 19
  CASE_D_EMPTY_WIND = 20
  CASE_U_EMPTY_WIND = 21

  CASE_R_EMPTY_CREVACE = 22
  CASE_L_EMPTY_CREVACE = 23
  CASE_D_EMPTY_CREVACE = 24
  CASE_U_EMPTY_CREVACE = 25

  CASE_R_EMPTY_MONSTER = 26
  CASE_L_EMPTY_MONSTER = 27
  CASE_D_EMPTY_MONSTER = 28
  CASE_U_EMPTY_MONSTER = 29
  
  PROBA_LOW = 30
  PROBA_MEDIUM = 31
  PROBA_HIGH = 32
  PROBA_SURE = 33
  
  PROBA_R_LOW = 34
  PROBA_R_MEDIUM = 35
  PROBA_R_HIGH = 36
  PROBA_R_SURE = 37
  
  PROBA_L_LOW = 38
  PROBA_L_MEDIUM = 39
  PROBA_L_HIGH = 40
  PROBA_L_SURE = 41
  
  PROBA_U_LOW = 42
  PROBA_U_MEDIUM = 43
  PROBA_U_HIGH = 44
  PROBA_U_SURE = 45
  
  PROBA_D_LOW = 46
  PROBA_D_MEDIUM = 47
  PROBA_D_HIGH = 48
  PROBA_D_SURE = 49




  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  def __init__(self, size):

    self.__size = size
    self.__facts = [[ Case() for i in range(self.__size) ] for j in range(self.__size)]
    self.initialisationNeighbour()
    self.initialisationFacts()

  def initialisationNeighbour(self):
    for i in range(self.__size):
      for j in range(self.__size):
        if j > 0 : self.__facts[i][j].caseL = self.__facts[i][j-1]
        if j < self.__size - 1 : self.__facts[i][j].caseR = self.__facts[i][j+1]
        if i > 0 : self.__facts[i][j].caseU = self.__facts[i-1][j]
        if i < self.__size - 1 : self.__facts[i][j].caseD = self.__facts[i+1][j]


  def initialisationFacts(self):
    for i in range(self.__size):
      for j in range(self.__size):
        self.__facts[i][j].addFact(self.EMPTY_BELIEF)
    self.__facts[0][0].removeFact(self.EMPTY_BELIEF)
    self.__facts[0][0].addFact(self.EMPTY)
    




  # ================================================================================================
  # PUBLIC METHODS
  # ================================================================================================

  def getFactsArray(self):
    return self.__facts


class Case:


  def __init__(self):
    self.__facts = []
    self.caseR = None
    self.caseD = None
    self.caseU = None
    self.caseL = None

  def addFact(self, fact):
    if not fact in self.__facts : self.__facts.append(fact)
    else : return False

  def removeFact(self,fact):
    if fact in self.__facts : self.__facts.remove(fact)

  def getFacts(self):
    return self.__facts
  
  def isParticularFact(self,fact):
    if fact in self.__facts : return True
    return False
  
  def areFactsEqual(self,fact1,fact2):
    if fact1 == fact2 :
      return True
    return False
 