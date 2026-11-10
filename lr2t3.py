class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other: 'Vector2D') -> bool:
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y

    def __abs__(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __len__(self) -> int:
        return 2

    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Індекс вектора поза межами діапазону (допустимі 0 або 1)")


v1 = Vector2D(3.0, 4.0)
v2 = Vector2D(1.0, 2.0)

print(str(v1))
print(repr(v1))

v3 = v1 + v2
print(v3)

v4 = v1 - v2
print(v4)

print(v1 == Vector2D(3.0, 4.0))
print(abs(v1))
print(len(v1))
print(v1[0], v1[1])
