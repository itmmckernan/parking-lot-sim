class Spot:
    occupant = None

    def __init__(self, parking, number):
        self.parking = parking
        self.number = number


    def clear(self):
        self.occupant = None

    def claim(self, occupant):
        if self.occupied():
            BlockingIOError('Spot Forcefully taken')
        self.occupant = occupant

    def occupied(self):
        return self.occupant is not None
