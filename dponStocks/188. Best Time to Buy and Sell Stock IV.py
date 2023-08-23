k = 2
prices = [2,4,1]

def bestprofit(prices, k):
    return solve(0, 1, k, prices)

def solve(ind, buy, cap, prices):
    if ind == len(prices):
        return 0
    
    if cap == 0:
        return 0
    profit = 0
    if buy:
        profit = max(-prices[ind] + solve(ind+1, 0, cap, prices), solve(ind+1, 1, cap, prices))
    else:
        profit = max(prices[ind] + solve(ind+1, 1, cap-1, prices), solve(ind+1, 0, cap, prices))
    return profit
print(bestprofit(prices, k))