arr= [1,2,3,2]

def missingRepeated(arr):
    n = len(arr)
    mp = {}
    Sum = 0
    ans = []
    for i in arr:
        mp[i] = mp.get(i, 0)+1
        
    # print(mp)
    
    for key, value in mp.items():
        if value == 2:
            ans.append(key)
            arr.remove(key)
            
    
    for i in arr:
        Sum = Sum + i
    totalSum = (n*(n+1))//2
    missingEl = totalSum - Sum
    
    ans.append(missingEl)
        
    
    return ans
print(missingRepeated(arr))