x = 4

def sqrt(x):
    low = 1
    hi = x
    
    while low <= hi:
        midpoint=(low+hi)//2
        if midpoint*midpoint <= x:
            low = midpoint+1
        else:
            hi = midpoint-1
    return hi

print(sqrt(x))