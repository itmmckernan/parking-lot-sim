from spot import Spot
import math

class Road:

    def __init__(self, length, ends=None, parking=False, points=None):
        self.spots = [Spot(parking, i) for i in range(length)]
        self.ends = ends
        self.parking = parking
        self.points = points

    def getNextSpot(self, spot):
        return self.spots[self.spots.index(spot)+1]

    def isSpotEnd(self, spot):
        return len(self.spots)-1 == self.spots.index(spot)

    def getPointPos(self, spot):
        pos = self.spots.index(spot)/len(self.spots)
        vector = ((self.points[0][0]-self.points[1][0]), (self.points[0][1]-self.points[1][1]))
        return self.points[0][0] - pos * vector[0], self.points[0][1] - pos * vector[1]
