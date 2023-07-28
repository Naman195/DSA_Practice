nums = [1,2,3,1]
k = 3

def Dups(nums, k):
    mp = {}
    for i in range(len(nums)):
        if nums[i] not in mp:
            mp[nums[i]]= i
        else:
            ind_diff = i - mp[nums[i]]
            if ind_diff <= k:
                return True
            mp[nums[i]] = i
    
    return False
print(Dups(nums, k))
        