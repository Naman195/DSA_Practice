row = 5
col = 3

def ncr(row, col):
    res = 1
    for i in range(col):
        res = res * (row-i)
        res = res//(i+1)
    return res

print(ncr(4, 2))