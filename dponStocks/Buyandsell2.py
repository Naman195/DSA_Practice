prices = [1,2,3,4,5]

def maxProfit(prices):
    return solve(0, 1, prices)

def solve(ind, buy, prices):
    if ind == len(prices):
        return 0
    
    profit = 0
    
    if(buy):
        profit = max(-prices[ind] + solve(ind+1, 0, prices), 0 + solve(ind+1, 1, prices))
    else:
        profit = max(prices[ind] + solve(ind+1, 1, prices), 0 + solve(ind+1, 0, prices))
    return profit

print(maxProfit(prices))
        
    