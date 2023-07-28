from heapq import *

target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]

def minimumFuelStation(stations, startFuel, target):
    n = len(stations)
    v = []
    v.append(target)
    v.append(0)
    stations.append(v)
    
    pq = []
    ans = 0
    
    for i in range(n):
        if stations[i][0] > startFuel:
            while startFuel < stations[i][0] and pq:
               
                startFuel += -heappop(pq)
                ans += 1
            
        if stations[i][0] > startFuel:
            return -1
        
        heappush(pq, -stations[i][1])
    return ans

print(minimumFuelStation(stations, startFuel,  target))
