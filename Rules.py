from Facts import Facts



class Rules:


	# ================================================================================================
	# CONSTRUCTOR
	# ================================================================================================
	def __init__(self):
		self.__rules == []
	  

	# def coverRules(self, facts):
	# 	activableRules = []
	# 	for values in self.__rules.values():
	# 		isRuleActivable = True
	# 		for i in range(len(values[0])):
	# 			j = 0
	# 			for fact in facts.getFacts() :
	# 				# égalité des faits ?
	# 				if facts.areFactsEqual(fact, values[0][i]) :
	# 					break
	# 				else :
	# 					j+=1
	# 			if j == len(facts) : #règle non valide
	# 				isRuleActivable = False
	# 				break # pour les values
	# 		if isRuleActivable :
	# 			activableRules.append(values)
	# 	return activableRules
