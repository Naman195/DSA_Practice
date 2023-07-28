nums = [10,5,2,6]
k = 100

def SubArrayProduct(nums, k):
    i = 0
    j = 0
    wMul = 1
    count = 0
    
    
    while j < len(nums):
        wMul = wMul * nums[j]
        if wMul >= k:
            while wMul >= k and i < len(nums):
                wMul //= nums[i]
                i += 1
            # j += 1
        
        if wMul < k:
            count += (j-i+1)
            j += 1
    return count
            
print(SubArrayProduct(nums, k))