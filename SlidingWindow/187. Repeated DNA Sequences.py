s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

def DnaSeq(s):
    seen = set()
    res = set()
    
    for i in range(len(s)-9):
        subseq = s[i:i+10]
        if subseq in seen:
            res.add(subseq)
        else:
            seen.add(subseq)
    
    return list(res)

print(DnaSeq(s))