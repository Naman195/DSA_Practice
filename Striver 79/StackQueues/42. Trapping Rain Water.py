height = [0,1,0,2,1,0,1,3,2,1,2,1]

def trap(arr):
    n = len(arr)
    prefix = [0]*n
    suffix = [0]*n
    
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = max(prefix[i-1], arr[i])
    
    suffix[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        suffix[i] = max(suffix[i+1], arr[i])
    
    waterTrapped = 0
    for i in range(n):
        waterTrapped += min(prefix[i], suffix[i]) - arr[i]
    return waterTrapped

print(trap(height))
        












# def ngel(arr):
#     n  = len(arr)
#     ans = [-1]*n
#     stack = []
    
#     for i in range(n):
#         while stack and stack[-1] <= arr[i]:
#             stack.pop()
        
#         if len(stack) == 0:
#             ans[i] = 0
#         else:
#             ans[i] = stack[-1]
#         stack.append(arr[i])
#     return ans

# def nger(arr):
#     n  = len(arr)
#     ans = [-1]*n
#     stack = []
    
#     for i in range(n-1, -1, -1):
#         while stack and stack[-1] <= arr[i]:
#             stack.pop()
        
#         if len(stack) == 0:
#             ans[i] = 0
#         else:
#             ans[i] = stack[-1]
#         stack.append(arr[i])
#     return ans

# arr = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(ngel(arr))
# print(nger(arr))

# def trappingWater(heights):
#     n = len(heights)
#     waterTrapped = 0
#     left = ngel(heights)
#     right = nger(heights)   
    
#     for i in range(n):
#         waterTrapped += (min(left[i], right[i]) - heights[i])
#     return waterTrapped

# print(trappingWater(height))

