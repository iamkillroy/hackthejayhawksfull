from .entity import Entity


class Heart:
	def __init__(self, x, y, screen):
		self.entityName = "hearts"
		super().__init__(x, y, screen)
		self.health = 8