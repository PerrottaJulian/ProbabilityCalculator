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
  M = 0
  
  for i in range (num_experiments): #one experiment each
    parcial = 0
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)
    
    for color, amount in expected_balls.items():
      if balls_drawn.count(color) >= amount :
        parcial += 1
        
    if parcial == len(expected_balls):
      M += 1
        
  return M/num_experiments
