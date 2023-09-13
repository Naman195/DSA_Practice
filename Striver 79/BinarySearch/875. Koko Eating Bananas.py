piles = [3,6,7,11]
h = 8

import math
def hourCount(arr, h):
    n = len(arr)
    totalH = 0
    for i in range(n):
        totalH += math.ceil(float(arr[i])/float(h))
    return totalH

        

def kokoeating(piles, h):
    low = 1
    high = max(piles)
    while low <= high:
        mid = (low + high)//2
        
        totalHour = hourCount(piles, mid)
        if totalHour <= h:
            high = mid-1
        else:
            low = mid+1
    return low
print(kokoeating(piles, h))
    