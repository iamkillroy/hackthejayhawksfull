
from pygame import Clock
from .entity import Entity 
class Enemy(Entity):
	def __init__(self, x, y, screen, health):
		self.entityName = "enemy"
		super().__init__(x, y, screen)
		self.health = health
		self.cooldown = 2
		self.coordNodes = [{"x": 300, "y": 300}]
		self.currentCoordNodes = 0
		self.x = 300
		self.y = 300
	def update(self):
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
		print(self.x)
		print(self.y)
		print("fact")
		if round(self.x) > round(self.coordNodes[0]["x"]) or round(self.x) < round(self.coordNodes[0]["x"]):
			ammountX = -1 if self.x-self.coordNodes[0]["x"] > 0 else 1
			self.x = ammountX + self.x
		if round(self.y) > round(self.coordNodes[0]["y"]) or round(self.y) < round(self.coordNodes[0]["y"]):
			ammountY = -1 if self.y-self.coordNodes[0]["y"] > 0 else 1
			self.y = ammountY + self.y
		else: #if all is false, we're at the right point and += 1 
			self.currentCoordNodes += 1 if self.currentCoordNodes < len(self.coordNodes) else 0
		super().update()