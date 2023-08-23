# Step 1: Find the Break Point eg = [2,1 | , 5,4,3,0,0] (A[i] < A[i+1])

# Step2: find  > ind but one of that you stay close
# step3 : Try to Place in Sorted Order (ind+1: n-1)

def nextPermu(nums):
    n = len(nums)
    ind = -1
    for i in range(n-2, -1, -1):
        if(nums[i] < nums[i+1]):
            ind = i
            break
    if ind == -1:
        return nums.reverse()
    
    for i in range(n-1, ind, -1):
        if nums[i] > nums[ind]:
            nums[ind], nums[i] = nums[i], nums[ind]
            break
    
    nums[ind+1: ] = reversed(nums[ind+1: ])
    return nums
A = [2, 1, 5, 4, 3, 0, 0]
print(nextPermu(A))
    
    
        