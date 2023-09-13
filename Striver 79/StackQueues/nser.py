arr = [4,6,7,1,2,9,0]

def nger(arr):
    n = len(arr)
    stack = []
    ans = [-1]*n
    
    for i in range(n-1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        
        if len(stack) == 0:
            ans[i] = -1
        else:
            ans[i] = stack[-1]
        
        stack.append(arr[i])
    return ans
print(nger(arr))