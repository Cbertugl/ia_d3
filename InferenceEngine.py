from Fact import Fact
import random
import rules

class InferenceEngine:

  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  def __init__(self):
    self.__rules = rules.rules


  # ================================================================================================
  # PUBLIC FUNCTIONS
  # ================================================================================================
  def run(self, facts):
    # Init
    over = False
    inferenceFacts = facts.copy()
    for r in self.__rules:
      r.unmark()

    while(not over):
      over = True

      # Select applicable rules (not marked, no contradiction and possible)
      applicableRules = []

      for r in self.__rules:
        if(
          not r.isMarked() and
          r.isPossible(inferenceFacts)
        ):
          if(r.hasContradiction(inferenceFacts)):
            r.mark()
          else:
            applicableRules.append(r)

      # Choose which rule we apply according to priority or randomly if
      # they all have the same priority
      if(len(applicableRules) > 0):
        over = False
        maxPriority = 0
        bestRule = None

        for r in applicableRules:
          if(r.getPriority() > maxPriority):
            maxPriority = r.getPriority()
            bestRule = r

        if(bestRule == None):
          bestRule = applicableRules[random.randint(0, len(applicableRules) - 1)]

        # Apply rule
        newFacts = bestRule.getConclusion(inferenceFacts)
        for f in newFacts:
          Fact.addFact(f, inferenceFacts)

        bestRule.mark()

    return inferenceFacts
