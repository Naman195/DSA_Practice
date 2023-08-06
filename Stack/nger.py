def nger(arr):
    n = len(arr)
    ans = [-1]*n
    stack = []
    for i in range(n-1, -1 , -1):
        while(len(stack) != 0 and stack[-1] <= arr[i]):
            stack.pop()
        
        if(len(stack) == 0):
            ans[i] = -1
        else:
            ans[i] = stack[-1]
        stack.append(arr[i])
    
    return ans

arr = [4,6,7,1,2,9,10]

print(nger(arr))