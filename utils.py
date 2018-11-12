import random

def getRandomPosition(size):
  return (random.randint(0, size - 1), random.randint(0, size - 1))

# Given a chance in %, return True if you win and False otherwise
def rollDice(chance):
  r = random.uniform(0, 100)

  if(r < chance):
    return True
  else:
    return False
