from Facts import SeSituer

class Rules:


	# ================================================================================================
	# CONSTRUCTOR
	# ================================================================================================
	def __init__(self):
	  # Forest
	  self.__rules = [ ] # ["Si Fact A", "Alors Action B"] , [ "Si A2", "Alors B2"]
	  self.__posVar = (-1,-1)
	  factNumber1 = SeSituer("player",self.__posVar)
	  self.__addAFact(factNumber1)



	def __addAFact(self, fact):
		self.__rules.append(fact)
