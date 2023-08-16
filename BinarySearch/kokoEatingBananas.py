piles = [3,6,7,11]
h = 8
import math
def HourCal(piles, h):
    totalHour = 0
    for i in range (len(piles)):
        totalHour += math.ceil((float(piles[i])) / float(h))
    return totalHour




def koko(piles, h):
    low = 1
    high = max(piles)
    
    while low <= high:
        mid =  (low +high)//2
        
        totalHour = HourCal(piles, mid)
        if(totalHour <= h):
            high = mid-1
        else:
            low = mid+1
    return low

print(koko(piles, h))
    