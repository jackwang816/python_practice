DYNAMIC_PROGRAMMING = 'dynamic programming'
GREEDY = 'greedy'

class MaxProfit(object):
    """
    Say you have an array for which the ith element is the price of a given stock on day i.
    If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
    Note that you cannot sell a stock before you buy one.
    """
    def __init__(self):
        self.solution_dict = {
            DYNAMIC_PROGRAMMING: self._dynamic_programming,
            GREEDY: self._greedy,
        }

    def solution(self, prices: list, solution: str=DYNAMIC_PROGRAMMING) -> int:
        return self.solution_dict[solution](prices)

    def _dynamic_programming(self, prices: list) -> int:
        """
        transfer prices list: let (i>j)
            profit{j~i} = p[i]-p[j] = (p[i]-p[i-1])+(p[i-1]-p[i-2])+...+(p[j+1]-p[j])
            let: delta[i] = p[i]-p[i-1] (i>0), delta[0]=0 means no transaction happened
            profit{j~i} = delta[j]+delta[j+1]+...+delta[i-1]+delta[i]
            now maxProfit = maxSubarray of delta
        """
        if len(prices) < 2:
            return 0 # not enough prices for transaction
        delta = [
            prices[i] - prices[i-1] if i > 0 else 0
            for i in range(len(prices))
        ]
        max_profit = delta[0]
        max_sum = 0
        for d in delta:
            max_sum = max(d, max_sum+d)
            max_profit = max(max_sum, max_profit)
        return max_profit

    def _greedy(self, prices: list) -> list:
        if len(prices) < 2:
            return 0 # not enough prices for transaction
        buy, max_profit = prices[0], 0
        for p in prices:
            buy, max_profit = min(p, buy), max(max_profit, p-buy)
        
        return max_profit

def test_max_profit_dp(test_cases, maxProfit):
    for t in test_cases:
        print(maxProfit.solution(t[0]))
        assert(maxProfit.solution(t[0])==t[1])

def test_max_profit_greedy(test_cases, maxProfit):
    for t in test_cases:
        print(maxProfit.solution(t[0], GREEDY))
        assert(maxProfit.solution(t[0], GREEDY)==t[1])

def test_max_profit():
    test_cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
    ]
    maxProfit = MaxProfit()
    test_max_profit_dp(test_cases, maxProfit)
    test_max_profit_greedy(test_cases, maxProfit)

if __name__ == "__main__":
    test_max_profit()
    x, y = 1, 2
    x, y = max(x, y), x-y
    print(x, y)