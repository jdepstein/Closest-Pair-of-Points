# HW 3
# Trey and Josh
# Point Class

from __future__ import annotations
import math
import random


class Point:

    def __init__(self, x: float, y: float):

        """
        :param x: The x coordinate of a point
        :param y: The y coordinate of a point
        """
        self.x = x
        self.y = y

    def getx(self) -> float:

        """
        :return: The x coordinate of the point
        """
        return self.x

    def gety(self) -> float:

        """
        :return: The y coordinate of the point
        """
        return self.y

    def get_dist(self, other: Point) -> float:

        """
        :param other: A point we want to know how far away it is from the current Point
        :return:A float distance using the distance of two points formula
        """
        return math.sqrt((other.getx() - self.x)**2 + (other.gety() - self.y)**2)

    def print_point(self) -> (float, float):

        """
        :return: a tuple of the x and y coordinates
        """
        return self.x, self. y


# These exist so we can use the python's built in sort function which is time complexity n(log(n))
# Point will sort on the x value. It is very easy to change it to sort on the y value though
    def __eq__(self, other: Point) -> bool:

        """
        :param other: A point that is being used to compare
        :return: True if the points x values are equal False if they are not equal
        """
        return self.x == other.getx()

    def __lt__(self, other: Point) -> bool:

        """
        :param other: A point that is being used to compare
        :return: True if the x value is less than the other points x False if not
        """

        return self.x < other.getx()

    def __gt__(self, other: Point) -> bool:

        """
        :param other: A point that is being used to compare
        :return: True if the x value is greater than the other points x False if not
        """
        return self.x < other.getx()

