

class Enemy(Entity):
	def __init__(self, x, y, screen, health):
		super.__init__(self, x, y, screen)
		self.health = health
		self.cooldown = 2
		self.coordNodes = [(0,0,), (100,100), (200,200), (300,300)]
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