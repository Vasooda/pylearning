import random

class Die:
  def __init__(self,sides=6):
    self.sides = sides

  def roll_die(self):
    results = random.randint(1,self.sides)
    print(f"Your dice rolled:{results}")

  def roll_die_10_times(self):
    dice = list(range(1,6))
    results = random.choices(dice,k=10)
    print(results)

  def roll_10side_die(self):
    dice2 = list(range(1,10))
    results = random.choices(dice2,k=10)
    print(results)

  def roll_20side_die(self):
    dice3 = list(range(1,20))
    results = random.choices(dice3,k=10)
    print(results)
  

player = Die()
player.roll_die()
player.roll_die_10_times()
player.roll_10side_die()
player.roll_20side_die()
