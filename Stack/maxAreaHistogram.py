heights = [2,1,5,6,2,3]
def maxArea(heights):
    leftSmaller = [0]*len(heights)
    rightSmaller = [0]*len(heights)
    
    stack = []
    n = len(heights)
    
    #nextt
    # for i in range(len(heights)):
    #     while stack and heights[stack[-1]] >= heights[i]:
    #         stack.pop()
        
    #     if len(stack) == 0:
    #         leftSmaller[i]= 0
    #     else:
    #         leftSmaller[i] = stack[-1]+1
    #     stack.append(i)
    
    # stack = []
    for i in range(n-1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
            
        if len(stack) == 0:
            rightSmaller[i] =  n-1
        
        else:
            rightSmaller[i] = stack[-1]-1
        stack.append(i)
    
    # print(leftSmaller)
    print(rightSmaller)
print(maxArea(heights))