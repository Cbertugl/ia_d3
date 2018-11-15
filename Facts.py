from abc import ABC, abstractmethod


class Facts:

  SAPE_UP = 0
  SAFE_DOWN = 1
  SAFE_LEFT = 2
  SAFE_RIGHT = 3

  WALL_UP = 4
  WALL_DOWN = 5
  WALL_LEFT = 6
  WALL_RIGHT = 7

  POOP = 8
  WIND = 9
  LIGHT = 10

  MONSTER = 11
  CREVACE = 12



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




  # ================================================================================================
  # PUBLIC METHODS
  # ================================================================================================

  # def addAFact(self, fact):
  # 	self.__facts.append(fact)

  # def removeAFact(self,fact):
  # 	self.__facts.remove(fact)

  # def findAFact(self, newFact):
  # 	for fact in self.__facts :
  # 		if isinstance(newFact,SeSituer) and isinstance(fact,SeSituer) :
  # 			if newFact.getElem() == fact.getElem() and newFact.getPos() == fact.getPos():
  # 				return fact
  # 			elif newFact.getElem() == fact.getElem() and newFact.getElem() == "player":
  # 				return fact
  # 	return False

  # def areFactsEqual(self,fact1,fact2):
  # 	if isinstance(fact1,SeSituer) and isinstance(fact2,SeSituer) :
  # 			if fact1.getElem() == fact2.getElem() and fact1.getPos() == fact2.getPos():
  # 				return True
  # 	elif isinstance(fact1,Mort) and isinstance(fact2,Mort) :
  # 			if fact1.getElem() == fact2.getElem() :
  # 				return True
  # 	else : return False

  # def findAFactWithPosition(self,pos):
  # 	for fact in self.__facts:
  # 		if fact.getPos() == pos:
  # 			return fact
  # 	return False

  # def getFacts(self):
  # 	return self.__facts



class Fact:


  def __init__(self):
    self.__facts = []

  def addFact(self, fact):
    self.__facts.append(fact)
  
 

# class SeSituer(Fact):

# 	def __init__(self,elem,pos):
# 		super().__init__()
# 		self.__elem = elem
# 		self.__pos = pos

# 	def getElem(self):
# 		return self.__elem

# 	def getPos(self):
# 		return self.__pos


# # class Vivant(Fact):

# # 	def __init__(self,elem):
# # 		super().__init__()
# # 		self.__elem = elem

# class Mort(Fact):

# 	def __init__(self,elem):
# 		super().__init__()
# 		self.__elem = elem