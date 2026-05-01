
from pygame import Clock
from .entity import Entity
from .entsignal import SIG
class Enemy(Entity):
	def __init__(self, x, y, screen, health):
		self.entityName = "enemy"
		super().__init__(x, y, screen)
		self.health = health
		self.cooldown = 2
		self.coordNodes = [{"x": 1600, "y": 825}, {"x": 1600, "y": 500}, {"x": 100, "y": 500}, {"x": 100, "y": 75}, {"x": 2000, "y": 75}]
		self.currentCoordNodes = 0
		self.x = float(-50)
		self.y = float(825)
		self.speed = 100
	def update(self, dt):
		#this is our moving algo:
		# you can think of pretty much the shortest relative path as the distance between
		# x1,y1 (our xy) and x2,y2 (their xy)
		#
		#	 Y (2,2)
		#	/
		#  /
		# E
		# (1,1)
		# so now we pretty miuch have the position of x,y
		# and we're able to basically move the position from
		#dt = clock.tick(30) / 1000 #get deltatime TODO
		#check for x, y
		if round(self.x) > round(self.coordNodes[self.currentCoordNodes]["x"]) or round(self.x) < round(self.coordNodes[self.currentCoordNodes]["x"]):
			ammountX = -1 * self.speed if self.x-self.coordNodes[self.currentCoordNodes]["x"] > 0 else self.speed
			self.x = ammountX * dt + self.x
		elif round(self.y) > round(self.coordNodes[self.currentCoordNodes]["y"]) or round(self.y) < round(self.coordNodes[self.currentCoordNodes]["y"]):
			ammountY = -1 * self.speed if self.y-self.coordNodes[self.currentCoordNodes]["y"] > 0 else self.speed
			self.y = ammountY * dt + self.y
		else: #if all is false, we're at the right point and += 1
			self.currentCoordNodes += 1
			if not (self.currentCoordNodes < len(self.coordNodes)): #this'll hit when we exceed the path (AKA we're done)
				#now we gotta return the signal to kill us
				return SIG.killme,SIG.finishedCourse
		super().update(dt)
