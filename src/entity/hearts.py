from .entity import Entity
import pygame

class Heart(Entity):
	def __init__(self, x, y, screen):
		self.entityName = "hearts"
		super().__init__(x, y, screen)
		self.health = 8
		self.startX = x
		self.startY = y
		#this is a carbon copy of the previous gamemap rescale, look for comments there
		self.sprites = list()
		scaledHeart = pygame.transform.scale_by(pygame.image.load(self.get_sprite_addr(0)), 4)
		self.sprites.append(scaledHeart)
	def display(self):
	    pass
	def update(self, dt):
	    super().update(dt)
