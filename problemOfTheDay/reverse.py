s = 'Geeks'

def reverse(s):
   
    x = []
    for i in s:
        x.append(i)
    left = 0
    right = len(s)-1
    while left <= right:
        temp = x[left]
        x[left] = x[right]
        x[right] = temp
        
                
        left += 1
        right -= 1
    print(x)
    return "".join(x)

print(reverse(s))

