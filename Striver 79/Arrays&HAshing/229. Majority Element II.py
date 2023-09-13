def majorityEle(nums):
    n = len(nums)
    mp = {}
    ans = []
    for i in nums:
        mp[i] = mp.get(i,0)+1
        
    print(mp)
    for key, value in mp.items():
        if value > n//3:
            ans.append(key)
    return ans


    
nums = [1,2]
print(majorityEle(nums))