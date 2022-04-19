class Car:
    done = False
    taskTicks = 0
    turnNum = 0
    def __init__(self, road, finalSpot, turns, number, currentSpot=None):
        self.road = road
        self.finalSpot = finalSpot
        self.turns = turns
        self.currentSpot = currentSpot
        self.number = number

    def getPoint(self):
        point = self.road.getPointPos(self.currentSpot)
        done = self.done and self.taskTicks == 0
        offset_y = 0 if not done else (50 if self.turns[-1] else -50)
        offset_x = 0 if not done else 25
        return point[0] + offset_x, point[1] + offset_y


    def tick(self):
        if self.taskTicks:
            self.taskTicks -= 1
            return

        if self.done:
            if not self.currentSpot is None:
                self.currentSpot.clear()
            return

        if self.currentSpot is None:
            if not self.road.spots[0].occupied():
                print(f'car {self.number} got first spot')
                self.currentSpot = self.road.spots[0]
                self.currentSpot.claim(self)
            else:
                print(f'car {self.number} waiting for first spot')
        elif self.road.parking and self.currentSpot.number == self.finalSpot:
            print(f'car {self.number} done')
            self.taskTicks = 5
            self.done = True
        elif self.road.isSpotEnd(self.currentSpot) and not self.road.ends[self.turns[self.turnNum]].spots[0].occupied():
            print(f'car {self.number} changed roads')
            self.road = self.road.ends[self.turns[self.turnNum]]
            self.currentSpot.clear()
            self.currentSpot = self.road.spots[0]
            self.currentSpot.claim(self)
            self.turnNum += 1
        elif not self.road.isSpotEnd(self.currentSpot) and not self.road.getNextSpot(self.currentSpot).occupied():
            print(f'car {self.number} moved forwards')

            self.currentSpot.clear()
            self.currentSpot = self.road.getNextSpot(self.currentSpot)
            self.currentSpot.claim(self)
        else:
            print(f'car {self.number} cant move')

