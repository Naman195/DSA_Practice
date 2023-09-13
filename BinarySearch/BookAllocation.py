arr = [12,34,67,90]
stu = 2

def PagesCount(arr, pages):
    pagesStudent = 0
    Student = 1
    
    for i in range(len(arr)):
        if pagesStudent + arr[i] <= pages:
            pagesStudent += arr[i]
        else:
            Student += 1
            pagesStudent = arr[i]
    return Student

def bookAllocate(arr, stu):
    if stu > len(arr):
        return -1
    low = max(arr)
    high = sum(arr)
    
    while low <= high:
        mid = (low + high)//2
        
        pages = PagesCount(arr, mid)
        
        if pages > stu:
            low = mid+1 
        else:
            high = mid-1
            
            
    return low
print(bookAllocate(arr, stu))