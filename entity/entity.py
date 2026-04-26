import pygame


class Entity:
    def __init__(self, x, y) -> None:
        self.x = 0
        self.y = 0
        self.sprite = 0
        self.spriteState = 0
        self.entityName = "entity"
        self.visible = True
        # get all sprites and load within the class object itself
        self.sprites: pygame.Surface = []
        spriteInitIterator = 0
        if self.entityName == "entity":
            raise Exception(
                "Entity was initalized with no name: default entity will not behave and is defunct"
            )
        while True:
            # this is built from scratch to remove dependencies
            # so i'm checking if a file exists by trying to read it but
            # if not, then we break because we've reached the end amount of sprites
            try:
                open(self.get_sprite_addr(spriteInitIterator), "r").close()
                # we didn't break (yet) so the sprite does exist
                # we're gonna now add it to the actual sprite list
                self.sprites.append(
                    pygame.image.load(self.get_sprite_addr(spriteInitIterator))
                )
                # now we're gonna loop again and again
            except FileNotFoundError:
                break  # the sprite doesn't exist so leave

    def get_sprite_addr(self, spriteState):
        """Gets the current active sprite for the entity"""
        return "/assets/sprites/" + self.entityName + str(spriteState) + ".png"

    def display(self, screen: pygame.screen):
        """Draws the current sprite state at the current x and y of the entity"""
        screen.blit(self.sprites[self.spriteState], (self.x, self.y))

    def update(self): ...
