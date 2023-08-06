arr = [2,1,5,6,2,3,1]

def nsel(arr):
    n = len(arr)
    stack = []
    ans = [-1]*n
    
    for i in range(n):
        while len(stack) != 0 and stack[-1] >= arr[i]:
            stack.pop()
        
        if len(stack) == 0:
            ans[i] = -1
        else:
            ans[i] = stack[-1]
        stack.append(arr[i])
    return ans
print(nsel(arr))