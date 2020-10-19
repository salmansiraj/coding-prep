class UndergroundSystem:

    def __init__(self):

        self.checkInTable = {}
        # id : (id, location, time)

        self.avgTable = {}
        # (location1 + location2) : (sumTime, count)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # if (id not in self.checkInTable):
        self.checkInTable[id] = [id, stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        # checkInTable[id] = (id, prevLocation, checkinTime)
        duration = t - self.checkInTable[id][2]
        stationPath = self.checkInTable[id][1] + stationName

        if (stationPath not in self.avgTable):
            self.avgTable[stationPath] = [duration, 1]
        else:
            self.avgTable[stationPath][0] += duration
            self.avgTable[stationPath][1] += 1

        self.checkInTable.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        stationPath = startStation + endStation
        return self.avgTable[stationPath][0] / self.avgTable[stationPath][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
