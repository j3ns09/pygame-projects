from dataclasses import dataclass

@dataclass
class vec2:
    x: float
    y: float

    def unpack(self): return (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return vec2(self.x * other, self.y * other)