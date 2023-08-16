
def IterativeBSearch(arr, target):
    low = 0
    high=len(arr)-1
    
    while low <= high:
        mid = (low + high)//2
        
        if(arr[mid] == target):
            return mid
        
        elif(arr[mid] > target):
            high = mid-1
        
        else:
            low = mid+1
    return -1

# recursive

def search(arr, target, low, high):
    
    if low > high: return -1
    
    
    mid = (low + high)//2
    if(arr[mid] == target):
        return mid
    elif(arr[mid] > target):
        return search(arr, target, low, mid-1)
    else:
        return search(arr, target, mid+1, high)

arr=  [0,12,13,25,56]

# print(IterativeBSearch(arr, 25))
print(search(arr, 12, 0, len(arr)-1))
