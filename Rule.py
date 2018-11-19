from Fact import Fact

class Rule:

  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  # ifList and thenList are Fact arrays
  def __init__(self, ifList, thenList, priority = 0):
    self.__if = ifList
    self.__then = thenList
    self.__priority = priority
    self.__marked = False


  # ================================================================================================
  # PRIVATE FUNCTIONS
  # ================================================================================================
  def __getAllPossiblePosition(self, facts):
    positions = []

    for fact in facts:
      position = fact.getPosition()
      self.setPosition(position)

      res = True
      for ifFact in self.__if:
        if(
          ifFact.getNot() == True and
          Fact.factListContains(facts, ifFact)
        ):
          res = False
        elif(
          ifFact.getNot() == False and
          not Fact.factListContains(facts, ifFact)
        ):
          res = False

      self.resetPosition()

      if(res):
        positions.append(position)

    return positions

  def __getPossiblePosition(self, facts):
    positions = self.__getAllPossiblePosition(facts)
    if(len(positions) == 0):
      return False
    else:
      return positions[0]


  # ================================================================================================
  # PUBLIC FUNCTIONS
  # ================================================================================================
  def getPriority(self):
    return self.__priority

  def isMarked(self):
    return self.__marked

  def mark(self):
    self.__marked = True

  def unmark(self):
    self.__marked = False

  def setPosition(self, position):
    if(position == None):
      return

    for fact in self.__if:
      fact.setPosition(position)

    for fact in self.__then:
      fact.setPosition(position)

  def resetPosition(self):
    for fact in self.__if:
      fact.resetPosition()

    for fact in self.__then:
      fact.resetPosition()

  # Return True if rule is possible, False otherwise
  def isPossible(self, facts):
    return(self.__getPossiblePosition(facts) != False)

  # Return True if there is no contradiction between rule and facts, False otherwise
  def hasContradiction(self, facts):
    positions = self.__getAllPossiblePosition(facts)

    if(len(positions) == 0):
      return False
    else:
      for position in positions:
        self.setPosition(position)

        for thenFact in self.__then:
          if(Fact.hasContradiction(facts, thenFact)):
            self.resetPosition()
            return True

        self.resetPosition()

    return False

  # Return rule conclusion which is a Fact array
  def getConclusion(self, facts):
    res = []
    positions = self.__getAllPossiblePosition(facts)

    for position in positions:
      self.setPosition(position)
      tmp = self.__then.copy()
      for f in tmp:
        copy = f.copy()
        copy.resetPositionVariable()
        copy.setInference()
        res.append(copy)
      self.resetPosition()

    return res

  def toString(self):
    print("IF ", end="")
    Fact.displayFacts(self.__if, end="")
    print(" THEN ", end="")
    Fact.displayFacts(self.__then)

