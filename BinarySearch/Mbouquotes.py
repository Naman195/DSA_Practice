bloomDay = [7,7,7,7,13,11,12,7]
m = 2
k = 3

def possible(arr, day, m, k):
    cnt = 0
    noOfBooke = 0
    
    for i in range(len(arr)):
        if arr[i] <= day:
            cnt += 1
        else:
            noOfBooke += (cnt//k)
            cnt  = 0
    noOfBooke += (cnt//k)
    return True if noOfBooke >= m else False

def bouquotes(bloomDay, m, k):
    low = min(bloomDay)
    high = max(bloomDay)
    
    while low <= high:
        day = (low + high)//2
        if possible(bloomDay, day, m, k):
            high = day-1
        else:
            low = day + 1
    return low
print(bouquotes(bloomDay, m, k)) 