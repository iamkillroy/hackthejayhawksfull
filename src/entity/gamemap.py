import pygame

from .entity import Entity


class GameMap(Entity):
    def __init__(self, x, y, screen) -> None:
        self.entityName = "gamemap"
        super().__init__(x, y, screen)
        # some special stuff here -- i wanna change the resolution of the map
        # without directly changing the file itself, so clear the sprite set
        self.sprites = list()
        # and now add a scaled down version
        scaledBackground = pygame.transform.scale_by(
            pygame.image.load(self.get_sprite_addr(0)), 0.67
        )
        self.sprites.append(scaledBackground)
