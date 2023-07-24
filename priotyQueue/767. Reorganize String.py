from heapq import *
s = "aab"

def reOrganizeString(s):
    maxHeap = []
    mp = {}
    
    for i in s:
        mp[i] = mp.get(i,0)+1
    
    
    for key , value in mp.items():
        heappush(maxHeap, (-value, key))
    
    ans = []
    while len(maxHeap) >= 2:
        value1, key1 = heappop(maxHeap)
        value2, key2 = heappop(maxHeap)
        
        ans.append(key1)
        ans.append(key2)
        
        frq1 = -value1
        frq2 = -value2
        
        frq1 -=1 
        frq2 -=1
        
        if(frq1 >0):
            heappush(maxHeap, (-frq1, key1))
        if(frq2 > 0):
            heappush(maxHeap, (-frq2, key2))
    
    
    
    if(len(maxHeap) == 0):
        return "".join(ans)
    
    else:
        value, key = heappop(maxHeap)
        freq = -value
        
        if(freq == 1):
            ans.append(key)
            return "".join(ans)
        else:
            return ""
    
        
        
        
        
        
print(reOrganizeString(s))