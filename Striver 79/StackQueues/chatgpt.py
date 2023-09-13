def ngel(arr):
    n = len(arr)
    ans = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans

def nger(arr):
    n = len(arr)
    ans = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans

def trappingWater(heights):
    n = len(heights)
    waterTrapped = 0
    left = ngel(heights)
    right = nger(heights)

    for i in range(n):
        if left[i] != -1 and right[i] != -1:
            waterTrapped += min(heights[left[i]], heights[right[i]]) - heights[i]
    return waterTrapped

height = [4, 2, 0, 3, 2, 5]
print(trappingWater(height))
