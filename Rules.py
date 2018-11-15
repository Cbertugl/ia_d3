from Facts import Facts



class Rules:

  ADD = 0
  REMOVE = 1

  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  def __init__(self,facts):
    self.__rules = [
                  [[facts.WALL_UP],[self.ADD, facts.NOT_SAFE_UP],[self.REMOVE, facts.SAFE_UP]], 
                  [[facts.WALL_DOWN],[self.ADD,facts.NOT_SAFE_DOWN],[self.REMOVE, facts.SAFE_DOWN]],
                  [[facts.WALL_LEFT],[self.ADD, facts.NOT_SAFE_LEFT],[self.REMOVE, facts.SAFE_LEFT]],
                  [[facts.WALL_RIGHT],[self.ADD,facts.NOT_SAFE_RIGHT],[self.REMOVE, facts.SAFE_RIGHT]],
                  
                  [[facts.NOT_SAFE_UP,facts.POOP],[self.ADD,facts.MONSTER]]
                  ]
  
  def coverRules(self,facts):
    activableRules = []
    for rule in self.__rules :
      isRuleActivable = True
      for i in range(len(rule[0])):
        j = 0
        for fact in facts.getFacts() :
          # égalité des faits ?
          if facts.areFactsEqual(fact, rule[0][i]) :
            break
          else :
            j+=1
        if j == len(facts.getFacts()) : #règle non valide
          isRuleActivable = False
          break 
      if isRuleActivable :
        activableRules.append(rule)
    return activableRules

  def executeInitialRules(self,facts):
    activableRules = self.coverRules(facts)
    for rule in activableRules :
      if len(rule) >= 1 :
        for k in range(1,len(rule[1])):
          if rule[1][0] == self.REMOVE :
            facts.removeFact(rule[1][k])
          elif rule[1][0] == self.ADD :
            facts.addFact(rule[1][k])
      if len(rule) >= 2 :
        for k in range(1,len(rule[2])):
          if rule[2][0] == self.REMOVE :
            facts.removeFact(rule[2][k])
          elif rule[2][0] == self.ADD :
            facts.addFact(rule[2][k])

