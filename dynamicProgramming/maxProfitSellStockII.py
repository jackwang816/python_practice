from functools import wraps

DYNAMIC_PROGRAMMING_LOW_MEMORY = 'dynamic programming lwo memory'
DYNAMIC_PROGRAMMING = 'dynamic programming'
GREEDY = 'greedy'
RECURSIVE = 'recursive'

def recursive_cache(fn):
    @wraps(fn)
    def wrapper(*args):
        result = args[0].cache.get(args[2])
        if not result:
            result = fn(*args)
            args[0].cache[args[2]] = result
        return result
    return wrapper

class MaxProfitII(object):
    """
    Say you have an array prices for which the ith element is the price of a 
    given stock on day i.
    Design an algorithm to find the maximum profit. You may complete as many
    transactions as you like (i.e., buy one and sell one share of the stock
    multiple times).

    Note: You may not engage in multiple transactions at the same time (i.e.,
          you must sell the stock before you buy again).

    Example 1:
        Input: [7,1,5,3,6,4]
        Output: 7
        Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5),
                     profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell
                     on day 5 (price = 6), profit = 6-3 = 3.
    """

    def __init__(self):
        self.solution_dict = {
            DYNAMIC_PROGRAMMING: self.dynamic_programming,
            GREEDY: self.greedy,
            RECURSIVE: self.recursive, 
        }

    def solution(self, prices: list, solution: str=RECURSIVE) -> int:
        return self.solution_dict[solution](prices)

    @recursive_cache
    def _recursive(self, prices: list, n: int) -> int:
        if n <= 1:
            return 0
        max_profit = self._recursive(prices, n-1)
        cur = prices[n-1]
        for i in range(n-1):
            if cur > prices[i]:
                max_profit = max(max_profit, 
                    cur-prices[i] + self._recursive(prices, i))
        return max_profit

    def recursive(self, prices: list) -> int:
        """ recursive with cache
        max_profit(n) = max(
            max_profit(n-1),
            prices[n]-prices[n-1]+max_profit(n-1),
            prices[n]-prices[n-2]+max_profit(n-2),
            ...
            prices[n]-prices[0]+max_profit(0),
        )
        Note: Solution include sell and buy in the same day,
              which means doing nothing in the day(ie. skip the day).
        """
        if len(prices) <= 1:
            return 0
        # for cache
        self.cache = {}
        return self._recursive(prices, len(prices))
    
    def greedy(self, prices: list) -> int:
        """ greedy
        dp[i] is max profit achieved in day i
        dp[i] = max(
            dp[i-1],
            prices[i]-prices[i-1] + dp[i-1], 
            ...
            prices[i]-prices[0] + dp[0]
            )
        let buy[i] = dp[i] - prices[i]
        dp[i] = max(dp[i-1], prices[i]+buy[i-1], ...prices[i]+buy[0])
              = max(dp[i-1], prices[i]+max(buy{0~i-1}))
        let maxbuy[i] = max(buy{0~i})
        maxbuy[i] = max(maxbuy[i-1], dp[i]-prices[i])
        dynamic programming transition function: dp[0]=0, maxbuy[0]=-prices[0]
            dp[i] = max(dp[i-1], prices[i]+ maxbuy[i-1])
            maxbuy[i] = max(maxbuy[i-1], dp[i]-prices[i])
        reducing the space to single variable: (init dp = 0, maxbuy=-prices[0]
            dp = max(dp, prices[i]+maxbuy)
            maxbuy = max(maxbuy, dp-prices[i])
        Note: Solution include sell and buy in the same day,
              which means doing nothing in the day(ie. skip the day).
        """
        n = len(prices)
        if n <= 1:
            return 0
        dp, maxbuy = 0, -prices[0]
        for p in prices[1:]:
            dp = max(dp, p + maxbuy)
            maxbuy = max(maxbuy, dp - p)
        return dp

    def dynamic_programming(self, prices: list) -> int:
        """ dynamic programming
        dp[i] is max profit achieved in day i
        dp[i] = max(
            dp[i-1], 
            prices[i]-prices[i-1] + dp[i-1], 
            ...
            prices[i]-prices[0] + dp[0]
            )
        Note: Solution include sell and buy in the same day,
              which means doing nothing in the day(ie. skip the day).
        """
        n = len(prices)
        if n <= 1:
            return 0
        dp = [0] * n
        for i in range(1, n):
            m_cur = dp[i-1]
            for j in range(0, i):
                if prices[i] > prices[j]:
                    m_cur = max(
                        m_cur,
                        prices[i] - prices[j] + dp[j]
                    )
            dp[i] = m_cur
        return dp[n-1]

def cooldown_cache(key):
    assert(isinstance(key, str))
    def descorator_func(func):
        @wraps(func)
        def wrapper_func(*args):
            cache = args[0]._cache[key]
            result = cache.get(args[2])
            if not result:
                result = func(*args)
                cache[args[2]] = result
            return result
        return wrapper_func
    return descorator_func

class MaxProfitSellStockWithCooldown(object):
    """
    Say you have an array for which the ith element is the price of a given 
    stock on day i. Design an algorithm to find the maximum profit. You may
    complete as many transactions as you like (ie, buy one and sell one share
    of the stock multiple times) with the following restrictions:

    You may not engage in multiple transactions at the same time (ie, you must
    sell the stock before you buy again). After you sell your stock, you cannot
    buy stock on next day. (ie, cooldown 1 day)
    
    Example:
        Input: [1,2,3,0,2]
        Output: 3 
        Explanation: transactions = [buy, sell, cooldown, buy, sell]
    """
    def __init__(self):
        self.solution_dict = {
            DYNAMIC_PROGRAMMING: self.dynamic_programming,
            DYNAMIC_PROGRAMMING_LOW_MEMORY: self.dynamic_programming_low_memory,
            # GREEDY: self.greedy,
            RECURSIVE: self.recursive,
        }
    
    def solution(self, prices: list, solution: str=RECURSIVE) -> int:
        return self.solution_dict[solution](prices)

    @cooldown_cache("sell")
    def _max_sell(self, prices: list, n: int) -> int:
        if n < 1:
            return 0
        return max(
            self._max_sell(prices, n-1),
            self._max_hold(prices, n) + prices[n-1]
        )
    @cooldown_cache("hold")
    def _max_hold(self, prices: list, n: int) -> int:
        if n < 1:
            return -prices[0]
        return max(
            self._max_hold(prices, n-1),
            self._max_sell(prices, n-2) - prices[n-1]
        )

    def recursive(self, prices: list) -> int:
        """ recursive
        max_hold(i): max profit when holding stock at day i
        max_sell(i): max profit when selled stock at day i
        max_hold(i) = max(
            max_hold(i-1), # holding stock at day i-1
            max_sell(i-2) - prices[i] # buying stock a day i, must not sell at day i-1
        )
        max_sell(i) = max(
            max_sell(i-1), # not holding stock at day i
            max_hold(i) + prices[i] # holding stock at day i and sell it (Note:
            sell and buy in the same day means doing nothing in the day, ie. skip the day)
        )
        max_profit = max_sell(n)
        """
        if len(prices) <= 1:
            return 0
        self._cache = {
            "sell": {},
            "hold": {},
        }
        return self._max_sell(prices, len(prices))

    def dynamic_programming(self, prices: list) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        max_hold, max_sell = [0] * n, [0] * n
        max_hold[0] = -prices[0]
        for i in range(1, n):
            # at first prices[-1] = 0 for max_sell[i-2]
            max_hold[i] = max(max_hold[i-1], max_sell[i-2]-prices[i])
            max_sell[i] = max(max_sell[i-1], max_hold[i] + prices[i])
        return max_sell[n-1]

    def dynamic_programming_low_memory(self, prices: list) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        max_hold, max_sell, max_sell_II = -prices[0], 0, 0
        for i in range(1, n):
            max_hold = max(max_hold, max_sell_II - prices[i])
            max_sell_II, max_sell = max_sell, max(max_sell, max_hold + prices[i])
        return max_sell

def test_max_profit_common(maxProfit, test_cases):
    for solution in maxProfit.solution_dict:
        print('Test with solution: {}'.format(solution))
        for t in test_cases:
            print(maxProfit.solution(t[0], solution))
            assert(maxProfit.solution(t[0], solution) == t[1])

def test_max_profit_II():
    test_cases = [
        ([7,1,5,3,6,4], 7),
        ([1,2,3,4,5], 4),
        ([7,6,4,3,1], 0),
        ([], 0),
        ([7,1,5,5,6,4], 5),
        ([7,1,5,6,4,7], 8),
    ]
    maxProfit = MaxProfitII()
    print('====test_max_profit_II====')
    test_max_profit_common(maxProfit, test_cases)

def test_max_profit_with_cooldown():
    test_cases = [
        ([1,2,3,0,2], 3),
        ([], 0),
        ([2], 0),
        ([7,6,4,3,1], 0),
        ([2,1,4], 3),
    ]
    maxProfit = MaxProfitSellStockWithCooldown()
    print('====test_max_profit_with_cooldown====')
    test_max_profit_common(maxProfit, test_cases)

if __name__ == "__main__":
    test_max_profit_II()
    test_max_profit_with_cooldown()
