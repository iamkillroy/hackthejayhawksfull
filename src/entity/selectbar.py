from .entity import Entity


class SelectBar(Entity):
    def __init__(self, x, y, screen) -> None:
        self.entityName = "selectbar"
        # select bar will always be in the same place
        # we throw away the x and y init
        x, y = 100, 200
        super().__init__(x, y, screen)

    def update(self, optionalArgumentList=list()):

        super().update()
