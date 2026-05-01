from pygame import Clock
from .entity import Entity
from .entsignal import SIG

class Enemy(Entity):
	def __init__(self, x, y, screen, health):
		self.entityName = "enemy"
		super().__init__(x, y, screen)
		self.health = health
		self.cooldown = 2
		self.coordNodes = [
			{"x": 1600, "y": 825},
			{"x": 1600, "y": 500},
			{"x": 100,  "y": 500},
			{"x": 100,  "y": 75},
			{"x": 2000, "y": 75},
		]
		self.currentCoordNodes = 0
		self.x = float(x)
		self.y = float(y)
		self.speed = 100

	def update(self, dt):
		target = self.coordNodes[self.currentCoordNodes]
		tx, ty = target["x"], target["y"]

		dx = tx - self.x
		dy = ty - self.y

		# How far we can travel this frame
		step = self.speed * dt

		if abs(dx) > 0.5:
			# Move along X first
			move = min(step, abs(dx))   # never overshoot
			self.x += move if dx > 0 else -move
		elif abs(dy) > 0.5:
			# Then move along Y
			move = min(step, abs(dy))   # never overshoot
			self.y += move if dy > 0 else -move
		else:
			# Close enough — snap exactly to node and advance
			self.x = float(tx)
			self.y = float(ty)
			self.currentCoordNodes += 1

			if self.currentCoordNodes >= len(self.coordNodes):
				return SIG.KILLME, SIG.FINISHEDCOURSE

		super().update(dt)
