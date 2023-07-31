s1 = "ab"
s2 = "eidbaooo"

def checkInclusion(s1, s2):
    mp = {}
    
    for i in s1:
        mp[i] = mp.get(i, 0)+1
    
    wStart = 0
    matched = 0
    # res = 0
    
    for wEnd in range(len(s2)):
        currChar = s2[wEnd]
        
        if currChar in mp:
            mp[currChar] -= 1
        
            if(mp[currChar] == 0):
                matched += 1
        
        if matched == len(mp):
            return True
        
        if(wEnd >= len(s1)-1):
            leftChar = s2[wStart]
            wStart += 1
            
            if leftChar in mp:
                if mp[leftChar] == 0:
                    matched -= 1
                
                mp[leftChar] = mp.get(leftChar, 0) +1 
    return False

print(checkInclusion(s1, s2))
                
        
    
    