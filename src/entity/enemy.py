
from pygame import clock
class Enemy(Entity):
	def __init__(self, x, y, screen, health):
		super.__init__(self, x, y, screen)
		self.health = health
		self.cooldown = 2
		self.coordNodes = [(0,0), (100,100), (200,200), (300,300)]
		self.currentCoordNodes = 0
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
		dt = clock.tick(30) / 1000 #get deltatime
		#check for x, y 
		if round(self.x) > round(self.currentCoordNodes[0][0]) 
		or round(self.x) < round(self.currentCoordNodes)[0][0]:
			self.x += 1 * dt #x
		elif round(self.y) > round(self.currentCoordNodes[0][1]) 
		or round(self.y) < round(self.currentCoordNodes)[0][1]:
			self.y += 1 * dt #y
		else: #if all is false, we're at the right point and += 1 
			self.currentCoordNodes += 1 if self.currentCoordNodes < self.coordNodes else 0
