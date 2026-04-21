class Entity:
    def __init__(self, x, y) -> None:
        self.x = 0
        self.y = 0
        self.sprite = 0
        self.entityName = "entity"
        self.visible = True

    def get_sprite(self):
        return "/assets/sprites/" + self.entityName + ".png"

    def update(self): ...
