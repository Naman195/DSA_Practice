nums = [2,3,-2,4]

def maxProd(nums):
    n = len(nums)
    suffix = 1
    pref = 1
    
    
    maxi = float('-inf')
    
    for i in range(n):
        if pref == 0:
            pref = 1
        if suffix == 0:
            suffix = 1
        
        pref = pref * nums[i]
        suffix = suffix * nums[n-i-1]
        
        maxi = max(maxi, max(pref, suffix))
    return maxi
print(maxProd(nums))
        
    