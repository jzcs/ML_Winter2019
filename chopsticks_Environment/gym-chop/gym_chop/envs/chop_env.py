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
            return 1
        if (self.state[1][0] + self.state[1][1]) == 0:
            return 2

    def step(self, target):
        if self.done == 1:
			print("Game Over")
			return [self.state, self.reward, self.done, self.add]

        pass

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
		for i in range(2):
			for j in range(2):
				print(self.state[i][j], end = " ")
			print("")
