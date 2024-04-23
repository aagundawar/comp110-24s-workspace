"""Defining a Class."""

from __future__ import annotations

__author__ = "730663390"


class Point:
    """Class Attributes."""

    def __init__(self, x_init: float, y_init: float):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutates the existing point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point