class Box2D:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def toDict(self):
        return {"x": self.x, "y": self.y, "width": self.width, "height": self.height}