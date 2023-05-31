class UndergroundSystem:

    def __init__(self):
        #id to station name and time
        self.chin = {} 
        self.ave =  {} #tuples of stations u -> v, to sum of intervals and number of intervals 
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.chin and t == self.id[id][1]:
            return
        self.chin[id] = (stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        x = self.chin[id]
        del self.chin[id]
        time = t - x[1]
        tup = (x[0],stationName) 
        if  tup not in self.ave:
            self.ave[tup] = [time,1]
        else:
            self.ave[tup][0]+=time
            self.ave[tup][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.ave[(startStation,endStation)][0]/self.ave[(startStation,endStation)][1]        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

