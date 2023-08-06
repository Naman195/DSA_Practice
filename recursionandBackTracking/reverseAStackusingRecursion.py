# x = [5,4,3,2,1]

# def insert(stk, el):
#     if len(stk)== 0:
#         stk.append(el)
#         return
    
#     tmp = stk.pop()
#     insert(stk, tmp)
#     stk.append(tmp)
#     return


# def reverse(stk):
#     if len(stk) <= 1:
#         return
#     tmp = stk.pop()
#     reverse(stk)
#     insert(stk, tmp)
#     return

# reverse(x)

# print(x)







def insert(stk, el):
    if len(stk) == 0:
        stk.append(el)
        return

    tmp = stk.pop()
    insert(stk, el)
    stk.append(tmp)
    


def reverse(stk):
    if len(stk) <= 1:
        return
    tmp = stk.pop()
    reverse(stk)
    insert(stk, tmp)
    


x = [5, 4, 3, 2, 1]
reverse(x)
print(x)
