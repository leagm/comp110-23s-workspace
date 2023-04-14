"""LS26 Magic Methods"""

class Point:
    x: float = 1.0
    y: float = 2.0


def __innit__(self, x: float, y:float):
    """Initialize a point with its x, y components."""
    self.x = x
    self.y = y


def scale_by(self, factor: float):
    self.x *= factor
    self.y *= factor


def scale(self, factor: float):
    scaled: Point = Point(self.x * factor, self.y * factor\
return scaled