from Fact import Fact
from Rule import Rule
from Square import Square
from utils import X, UP, DOWN, LEFT, RIGHT

emptyRulePriority = 40
monsterRulePriority = 60
crevasseRulePriority = 80

rules = [

  # ================================================================================================
  # TERMINAL RULES
  # ================================================================================================
  # EXIT => CAN_EXIT
  Rule(
    [ Fact(Square.EXIT, positionVariable=X) ],
    [ Fact(Fact.CAN_EXIT) ],
    100
  ),


  # ================================================================================================
  # NORMAL RULES
  # ================================================================================================
  # EMPTY => EMPTY
  Rule(
    [
      Fact(Square.EMPTY, positionVariable=X),
      Fact(Fact.WALL, positionVariable=UP, notOperator=True)
    ],
    [ Fact(Square.EMPTY, positionVariable=UP) ],
    emptyRulePriority
  ),
  Rule(
    [
      Fact(Square.EMPTY, positionVariable=X),
      Fact(Fact.WALL, positionVariable=DOWN, notOperator=True)
    ],
    [ Fact(Square.EMPTY, positionVariable=DOWN) ],
    emptyRulePriority
  ),
  Rule(
    [
      Fact(Square.EMPTY, positionVariable=X),
      Fact(Fact.WALL, positionVariable=LEFT, notOperator=True)
    ],
    [ Fact(Square.EMPTY, positionVariable=LEFT) ],
    emptyRulePriority
  ),
  Rule(
    [
      Fact(Square.EMPTY, positionVariable=X),
      Fact(Fact.WALL, positionVariable=RIGHT, notOperator=True)
    ],
    [ Fact(Square.EMPTY, positionVariable=RIGHT) ],
    emptyRulePriority
  ),

  # MONSTER_POOP => MONSTER
  Rule(
    [
      Fact(Square.MONSTER_POOP, positionVariable=X),
      Fact(Fact.WALL, positionVariable=UP, notOperator=True)
    ],
    [ Fact(Square.MONSTER, positionVariable=UP) ],
    monsterRulePriority
  ),
  Rule(
    [
      Fact(Square.MONSTER_POOP, positionVariable=X),
      Fact(Fact.WALL, positionVariable=DOWN, notOperator=True)
    ],
    [ Fact(Square.MONSTER, positionVariable=DOWN) ],
    monsterRulePriority
  ),
  Rule(
    [
      Fact(Square.MONSTER_POOP, positionVariable=X),
      Fact(Fact.WALL, positionVariable=LEFT, notOperator=True)
    ],
    [ Fact(Square.MONSTER, positionVariable=LEFT) ],
    monsterRulePriority
  ),
  Rule(
    [
      Fact(Square.MONSTER_POOP, positionVariable=X),
      Fact(Fact.WALL, positionVariable=RIGHT, notOperator=True)
    ],
    [ Fact(Square.MONSTER, positionVariable=RIGHT) ],
    monsterRulePriority
  ),

  # WIND => CREVASSE
  Rule(
    [
      Fact(Square.WIND, positionVariable=X),
      Fact(Fact.WALL, positionVariable=UP, notOperator=True)
    ],
    [ Fact(Square.CREVASSE, positionVariable=UP) ],
    crevasseRulePriority
  ),
  Rule(
    [
      Fact(Square.WIND, positionVariable=X),
      Fact(Fact.WALL, positionVariable=DOWN, notOperator=True)
    ],
    [ Fact(Square.CREVASSE, positionVariable=DOWN) ],
    crevasseRulePriority
  ),
  Rule(
    [
      Fact(Square.WIND, positionVariable=X),
      Fact(Fact.WALL, positionVariable=LEFT, notOperator=True)
    ],
    [ Fact(Square.CREVASSE, positionVariable=LEFT) ],
    crevasseRulePriority
  ),
  Rule(
    [
      Fact(Square.WIND, positionVariable=X),
      Fact(Fact.WALL, positionVariable=RIGHT, notOperator=True)
    ],
    [ Fact(Square.CREVASSE, positionVariable=RIGHT) ],
    crevasseRulePriority
  )
]
