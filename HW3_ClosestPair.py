from typing import List
from Point import Point
import math
import random
import time

# Brute Force function of the Closest Points
def closest_pair_brute(points: List[Point]) -> (Point, Point, float):

    """
    :param points: A list of points that we want to find the closest pair in
    :return: Two tuples that being the two points that are closest in the given list
    """
    best_pair = (points[0], points[1])      # preset the best pair to the first two values in the list
    best_distance = points[0].get_dist(points[1])    # preset the best to the distance between the first two points

    for i in range(len(points) - 1):                # read through all point Nested for loop (n - 1) => O(n)
        for j in range((i + 1), len(points)):               # (n - 1)(n - 1) => O(n^2)
            d1 = points[i].get_dist(points[j])

            if best_distance > d1:                      # check to see if current pair is better then the best_pair
                best_pair = (points[i], points[j])
                best_distance = d1

    (x, y) = best_pair
    return x, y, best_distance


# Closet pair DAC
def closest_pair_dac(points: List[Point]) -> (Point, Point, float):

    """
    :param points: A  List of points given by the user
    :return: A tuple of the two closest points and their distance
    """

    def midpairs(midpts: List[Point]) -> (Point, Point, float):

        """
        :param midpts: A list of points that are in the delta+-
        :return: returns the closest pair in the middle section along with its distance
        """

        midsort = sorted(midpts, key=lambda Point: Point.gety())          # sort list according to y
        dist_best = math.inf                      # set the starting distance to something very large
        pt1 = Point                               # Create two points
        pt2 = Point

        for i in range(len(midsort) - 1):         # Run through all points expect for the last one

            if i < len(midsort) - 7:              # Checks if there is 7 pts in front of index i

                for j in range(1, 8):             # finds the best pair out of the 7 pts ahead of each point midsort[i]
                    dist = midsort[i].get_dist(midsort[i + j])

                    if dist_best > dist:          # Sets the best_distance and pts
                        pt1 = midsort[i]
                        pt2 = midsort[i + j]
                        dist_best = dist
            else:                                               # if there are less then 7 points
                for j in range(i + 1, len(midsort)):
                    dist = midsort[i].get_dist(midsort[j])

                    if dist_best > dist:
                        pt1 = midsort[i]
                        pt2 = midsort[j]
                        dist_best = dist

        return pt1, pt2, dist_best              # return

    # Base Case
    if len(points) <= 3:
        return closest_pair_brute(points)

    left = points[:len(points)//2]          # split the list into left and right halves
    right = points[len(points)//2:]
    mid = len(points)//2                    # Keep track of the mid

    (r1, r2, r_dist) = closest_pair_dac(right)  # call the function on the two halves

    (l1, l2, l_dist) = closest_pair_dac(left)

    if r_dist >= l_dist:                       # If the left distance is smaller

        left = points[mid].getx() - l_dist     # get the range of x values within the distance from mid
        right = points[mid].getx() + l_dist
        midpts = []

        for p in points:                       # make a list of all the x that are within that range
            if left <= p.getx() <= right:

                midpts.append(p)

        (mid1, mid2, dist) = midpairs(midpts)  # Call midpairs on your new list

        if dist < l_dist:                      # Return the best between the mid and left
            return mid1, mid2, dist

        else:
            return l1, l2, l_dist

    # Same for the right side if it is smaller
    else:
        left = points[mid].getx() - r_dist
        right = points[mid].getx() + r_dist
        midpts = []

        for p in points:
            if left <= p.getx() <= right:
                midpts.append(p)

        (mid1, mid2, dist) = midpairs(midpts)

        if dist < r_dist:
            return mid1, mid2, dist

        else:
            return r1, r2, r_dist
