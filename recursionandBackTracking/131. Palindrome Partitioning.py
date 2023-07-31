s = "aabb"

def palindromePartioning(s):
    lst = []
    ps = []
    solve(0, s, ps, lst)
    return lst

def palindromeCheck(s, start, end):
    while start <= end:
        if(s[start] != s[end]):
            
            return False
        start += 1
        end -= 1
    return True


def solve(ind, s, ps, lst):
    if ind == len(s):
        lst.append(ps[:])
        return
    
    for i in range(ind, len(s)):
        if(palindromeCheck(s, ind, i)):
            ps.append(s[ind:i+1])
            solve(i+1, s, ps, lst)
            ps.pop()

print(palindromePartioning(s))