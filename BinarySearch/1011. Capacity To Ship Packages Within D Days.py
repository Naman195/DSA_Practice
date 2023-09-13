weights = [1,2,3,4,5,6,7,8,9,10]
days = 5


def findDays(weight, capacity):
    days = 1
    load = 0
    for i in range(len(weight)):
        if (load + weight[i] > capacity):
            days += 1
            load =   weight[i]
        else:
            load += weight[i]
    
    return days

def shipWithinDays(weight, days):
    low = max(weight)
    high = sum(weight)
    
    while low <= high:
        mid = (low + high)//2 
        if findDays(weight, mid) <= days:
            high = mid - 1
        else:
            low = mid+1
    return low

print(shipWithinDays(weights, days))