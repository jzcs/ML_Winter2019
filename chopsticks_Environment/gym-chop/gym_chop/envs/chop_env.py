import gym
from gym import error, spaces, utils
from gym.utils import seeding

class ChopStick(gym.Env):
  metadata = {'render.modes': ['human']}
  def __init__(self):
    self.state = []
    for i in range(2):
      self.state += [[]]
      for j in range(2):
        self.state[i] += [1]
    self.fingers = 5
    self.counter = 0
    self.done = 0
    self.add = [0, 0] #Player wincounts
    self.reward = 0

  def setFingers(self, f):
    self.fingers = f

  def check(self):
    if(self.counter<5): #minimal number to reach game completion
      return 0
    if (self.state[0][0] + self.state[0][1]) == 0:
      return 2 #p2 wins
    if (self.state[1][0] + self.state[1][1]) == 0:
      return 1 #p1 wins
    return 0

  def step(self, action):
  #Action 0:4 (LL, LR, RL, RR, Split)
    p = self.counter%2 #player
    o = (p+1)%2 #opponent
    c = action%2 #target card
    if self.done == 1:
      print("Game Over")
      return [self.state, self.reward, self.done, self.add]
    if action < 2: #LL, LR
      if self.state[p][0] == 0: #Prevent add 0 moves
        print("Invalid Step")
        return [self.state, self.reward, self.done, self.add]
      self.state[o][c] = (self.state[o][c] + self.state[p][0]) %self.fingers
    elif action < 4: #RL, RR
      if self.state[p][1] == 0:
        print("Invalid Step")
        return [self.state, self.reward, self.done, self.add]
      self.state[o][c] = (self.state[o][c] + self.state[p][1]) %self.fingers
    elif action == 4: #Split
      if ((self.state[p][0] == 0 and (self.state[p][1]%2) == 0)
            or (self.state[p][1] == 0 and (self.state[p][0]%2)==0) ):
        temp = (self.state[p][1]+self.state[p][0])/2
        self.state[p][0] = temp
        self.state[p][1] = temp
      else:
        print("Invalid Step")
        return [self.state, self.reward, self.done, self.add]
    #if(self.counter == 100):
    #self.done = 1;
    self.counter += 1
    self.render()
    return [self.state, self.reward, self.done, self.add]

  def reset(self):
    for i in range(2):
      for j in range(2):
        self.state[i][j] = 1
    self.counter = 0
    self.done = 0
    self.add = [0, 0]
    self.reward = 0
    return self.state

  def render(self):
    print(self.state)
    return
