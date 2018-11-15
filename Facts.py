from abc import ABC, abstractmethod


class Facts:

	# ================================================================================================
	# CONSTRUCTOR
	# ================================================================================================
	def __init__(self):
	  # Forest
	  self.__facts = []
	  self.__facts.append(SeSituer("player",(0,0)))



# 	# def seSituer(self, elem, pos):
# 		# if elem.pos = pos :


	# ================================================================================================
	# PUBLIC METHODS
	# ================================================================================================

	def addAFact(self, fact):
		self.__facts.append(fact)

	def removeAFact(self,fact):
		self.__facts.remove(fact)

	def findAFact(self, newFact):
		for fact in self.__facts :
			if isinstance(newFact,SeSituer) and isinstance(fact,SeSituer) :
				if newFact.getElem() == fact.getElem() and newFact.getPos() == fact.getPos():
					print("yooo, déjà laaaa")
					return True
		# if newFact in self.__facts : return fact # a réécrire
		return False

	def getFacts(self):
		return self.__facts



class Fact(ABC):

  def __init__(self):
    super().__init__()
  
 


class SeSituer(Fact):

	def __init__(self,elem,pos):
		super().__init__()
		self.__elem = elem
		self.__pos = pos

	def getElem(self):
		return self.__elem

	def getPos(self):
		return self.__pos


class Vivant(Fact):

	def __init__(self,elem):
		super().__init__()
		self.__elem = elem

class Mort(Fact):

	def __init__(self,elem):
		super().__init__()
		self.__elem = elem