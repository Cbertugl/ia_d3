from Facts import Facts
from Facts import Case


class Rules:

  ADD = 0
  REMOVE = 1

  ADJACENT_CASE_UP_EMPTY = 3
  ADJACENT_CASE_DOWN_EMPTY = 4
  ADJACENT_CASE_LEFT_EMPTY = 5
  ADJACENT_CASE_RIGHT_EMPTY = 6

  ADJACENT_CASE_MONSTER = 7
  ADJACENT_CASE_CREVACE = 8

  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  def __init__(self,facts):
    self.__rules = [
                  # [[facts.WALL_UP],[self.ADD, facts.NOT_SAFE_UP],[self.REMOVE, facts.SAFE_UP]], 
                  # [[facts.WALL_DOWN],[self.ADD,facts.NOT_SAFE_DOWN],[self.REMOVE, facts.SAFE_DOWN]],
                  # [[facts.WALL_LEFT],[self.ADD, facts.NOT_SAFE_LEFT],[self.REMOVE, facts.SAFE_LEFT]],
                  # [[facts.WALL_RIGHT],[self.ADD,facts.NOT_SAFE_RIGHT],[self.REMOVE, facts.SAFE_RIGHT]],
                  
                  # [[case.isParticularFact(facts.EMPTY),case.caseR.isParticularFact(facts.EMPTY_BELIEF)],[case.caseR.addFact(facts.EMPTY)]]
                  [[facts.EMPTY,facts.CASE_R_EMPTY_BELIEF],[facts.CASE_R_EMPTY,facts.PROBA_LOW]]

                  [[facts.POOP,facts.CASE_R_EMPTY_BELIEF],[facts.MONSTER,facts.PROBA_LOW]]
                  [[facts.POOP,facts.CASE_R_MONSTER,facts.PROBA_R_LOW],[facts.PROBA_MEDIUM]] # On vérifie les faits de notre case pour changer les faits de la case
                                                                                            # adjacente qui changera a son tour les faits de la case actuelle
                  [[facts.POOP,facts.CASE_R_MONSTER,facts.PROBA_R_MEDIUM],[facts.PROBA_HIGH]] 
                  [[facts.POOP,facts.CASE_R_MONSTER,facts.PROBA_R_HIGH],[facts.PROBA_SURE]] 
                  # [[facts.POOP],[self.ADJACENT_CASES__EMPTY]]

                  ]

  def changementCaseR(case,formerFact,newFact):
    case.caseR.addFact(newFact)
    case.caseR.removeFact(formerFact)
    # refaire les droites hauts bas gauches avec les nouvelles valeurs !!! pas dans cette fonction
  
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
