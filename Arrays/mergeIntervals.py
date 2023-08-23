intervals = [[1,3],[2,6],[8,10],[15,18]]

def merge(intervals):
    if len(intervals) < 2:
        return intervals
    
    intervals.sort(key = lambda x : x[0])
    
    mergeIntervals = []
    
    prevInterval = intervals[0]
    for i in range(1, len(intervals)):
        currInterval = intervals[i]
        if currInterval[0] <= prevInterval[1]:
            prevInterval[1] = max(prevInterval[1], currInterval[1])
        else:
            mergeIntervals.append(prevInterval)
            prevInterval = currInterval
    mergeIntervals.append(prevInterval)
    return mergeIntervals
print(merge(intervals))
    