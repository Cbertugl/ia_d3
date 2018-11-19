from Fact import Fact
from Rule import Rule
from Square import Square
from utils import X, UP, DOWN, LEFT, RIGHT

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
    [ Fact(Square.EMPTY, positionVariable=UP) ]
  ),
  Rule(
    [
      Fact(Square.EMPTY, positionVariable=X),
      Fact(Fact.WALL, positionVariable=DOWN, notOperator=True)
    ],
    [ Fact(Square.EMPTY, positionVariable=DOWN) ]
  ),
  Rule(
    [
      Fact(Square.EMPTY, positionVariable=X),
      Fact(Fact.WALL, positionVariable=LEFT, notOperator=True)
    ],
    [ Fact(Square.EMPTY, positionVariable=LEFT) ]
  ),
  Rule(
    [
      Fact(Square.EMPTY, positionVariable=X),
      Fact(Fact.WALL, positionVariable=RIGHT, notOperator=True)
    ],
    [ Fact(Square.EMPTY, positionVariable=RIGHT) ]
  ),

  # MONSTER_POOP => MONSTER
  Rule(
    [
      Fact(Square.MONSTER_POOP, positionVariable=X),
      Fact(Fact.WALL, positionVariable=UP, notOperator=True)
    ],
    [ Fact(Square.MONSTER, positionVariable=UP) ]
  ),
  Rule(
    [
      Fact(Square.MONSTER_POOP, positionVariable=X),
      Fact(Fact.WALL, positionVariable=DOWN, notOperator=True)
    ],
    [ Fact(Square.MONSTER, positionVariable=DOWN) ]
  ),
  Rule(
    [
      Fact(Square.MONSTER_POOP, positionVariable=X),
      Fact(Fact.WALL, positionVariable=LEFT, notOperator=True)
    ],
    [ Fact(Square.MONSTER, positionVariable=LEFT) ]
  ),
  Rule(
    [
      Fact(Square.MONSTER_POOP, positionVariable=X),
      Fact(Fact.WALL, positionVariable=RIGHT, notOperator=True)
    ],
    [ Fact(Square.MONSTER, positionVariable=RIGHT) ]
  ),

  # WIND => CREVASSE
  Rule(
    [
      Fact(Square.WIND, positionVariable=X),
      Fact(Fact.WALL, positionVariable=UP, notOperator=True)
    ],
    [ Fact(Square.CREVASSE, positionVariable=UP) ]
  ),
  Rule(
    [
      Fact(Square.WIND, positionVariable=X),
      Fact(Fact.WALL, positionVariable=DOWN, notOperator=True)
    ],
    [ Fact(Square.CREVASSE, positionVariable=DOWN) ]
  ),
  Rule(
    [
      Fact(Square.WIND, positionVariable=X),
      Fact(Fact.WALL, positionVariable=LEFT, notOperator=True)
    ],
    [ Fact(Square.CREVASSE, positionVariable=LEFT) ]
  ),
  Rule(
    [
      Fact(Square.WIND, positionVariable=X),
      Fact(Fact.WALL, positionVariable=RIGHT, notOperator=True)
    ],
    [ Fact(Square.CREVASSE, positionVariable=RIGHT) ]
  )
]
