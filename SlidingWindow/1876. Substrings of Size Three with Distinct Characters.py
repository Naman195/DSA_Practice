s = "xyzzaz"

def diffSubS(s):
    subString = []
    for i in range(len(s)-2):
        k = s[i:i+3]
        subString.append(k)
    # print(subString)
    ans = 0
    for i in subString:
        if(len(set(i)) == 3):
            ans += 1
    return ans
print(diffSubS(s))