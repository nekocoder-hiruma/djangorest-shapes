import math
import uuid
from django.db import models


class ShapeBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(db_index=True,
                            primary_key=True,
                            default=uuid.uuid4)
    name = models.CharField(max_length=200)


class Triangle(ShapeBase):
    base = models.IntegerField()
    adjacent = models.IntegerField()
    opposite = models.IntegerField()

    def __str__(self):
        return f"Triangle {self.name}"

    def area(self):
        half_perimeter = (self.base + self.adjacent + self.opposite) / 2
        heron_part_one = (half_perimeter - self.base) * (half_perimeter - self.adjacent) * (half_perimeter - self.opposite)
        return math.sqrt(half_perimeter * heron_part_one)

    def perimeter(self):
        return self.base + self.opposite + self.adjacent


class Square(ShapeBase):
    side = models.IntegerField()

    def __str__(self):
        return f"Triangle {self.name}"

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4


class Rectangle(ShapeBase):
    width = models.IntegerField()
    length = models.IntegerField()

    def __str__(self):
        return f"Rectangle {self.name}"

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (self.width * 2) + (self.length * 2)


class Diamond(ShapeBase):
    length = models.IntegerField()
    diagonal_one = models.IntegerField()
    diagonal_two = models.IntegerField()

    def __str__(self):
        return f"Diamond {self.name}"

    def area(self):
        return (self.diagonal_one * self.diagonal_two) / 2

    def perimeter(self):
        return self.length * 4
