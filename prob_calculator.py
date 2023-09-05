import copy
import random

class Hat:
  def __init__(self, **balls):
    self.contents = []
    for color, amount in balls.items():
      self.contents.extend([color for i in range(amount)])

  def draw(self, amount):
    drawed_balls = []
    for i in range(amount):
      ball = self.contents[random.randint(0,len(self.contents)-1)]
      self.contents.remove(ball)
      drawed_balls.append(ball)
    return drawed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  pass