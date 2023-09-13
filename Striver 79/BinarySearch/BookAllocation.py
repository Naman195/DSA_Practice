arr = [25, 46, 28, 49, 24]
n = 5
m = 4

def bookAllocate(arr, m):
    if m > len(arr):
        return -1
    low = max(arr)
    high = sum(arr)
    
    while low <= high:
        mid = (low + high) // 2
        
        Student = countStu(arr, mid)
        if Student > m:
            low = mid+1
        else:
            high = mid-1
        
    return low

def countStu(arr, pages):
    pagesStu = 0
    Student = 1
    
    for i in range(len(arr)):
        if pagesStu + arr[i] <= pages:
            pagesStu += arr[i]
        else:
            Student += 1
            pagesStu = arr[i]
    return Student
print(bookAllocate(arr, m))