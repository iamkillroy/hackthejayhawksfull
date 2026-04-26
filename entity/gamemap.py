from .entity import Entity


class GameMap(Entity):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.entityName = "gamemap"

    def update(self):
        self.draw()
