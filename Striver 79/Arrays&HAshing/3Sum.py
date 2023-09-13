nums = [-1,0,1,2,-1,-4]

def Sum3(nums):
    n = len(nums)
    nums.sort()
    ans = []
    
    for i in range(n):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        
        j = i+1
        k = n-1
        while j < k:
            curSum = nums[i] + nums[j] + nums[k]
            if curSum <  0:
                j += 1
            elif curSum > 0:
                k -=1
            else:
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)
                j += 1
                k -= 1
            
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                
                while j < k and nums[k] == nums[k+1]:
                    k -=1
                    
    return ans


print(Sum3(nums))
            
            
            
            
            
            
            