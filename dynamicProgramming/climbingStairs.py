from functools import wraps

BACK_TRACKING = 'backtracking'
DYNAMIC_PROGRAMMING = 'dynamic programming'

def cache_result(fn):
    cache = {}

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args)
        if not result:
            result = fn(*args)
            cache[args] = result
        return result
    return wrapper

class ClimbingStairs(object):
    def __init__(self):
        self.solution_dict = {
            BACK_TRACKING: self.back_tracking,
            DYNAMIC_PROGRAMMING: self.dynamic_programming,
        }

    def solution(self, n: int, solution:str=BACK_TRACKING) -> int:
        return self.solution_dict[solution](n)
    
    def dynamic_programming(self, n: int) -> int:
        prev = [1, 1]
        result = 1 if n >= 0 else 0
        for i in range(2, n+1):
            result = prev[0] + prev[1]
            prev[0], prev[1] = prev[1], result
        return result

    @cache_result
    def back_tracking(self, n:int) -> int:
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return 1
        return self.back_tracking(n-1) + self.back_tracking(n-2)

class MinCostClimbingStairs(object):
    def __init__(self):
        self.solution_dict = {
            BACK_TRACKING: self.back_tracking,
            DYNAMIC_PROGRAMMING: self.dynamic_programming,
        }

    def solution(self, costs:list, solution:str=BACK_TRACKING) -> int:
        n = len(costs)
        self.cache = [-1] * (n+1)
        return self.solution_dict[solution](costs, n)
    
    def dynamic_programming(self, cost:list, n: int) -> int:
        if n < 2:
            return 0
        prev = [cost[0], cost[1]]
        for c in cost[2:]:
            result = c + min(prev[0], prev[1])
            prev[0], prev[1] = prev[1], result
        return min(prev[0], prev[1])

    def back_tracking(self, costs: list, n:int) -> int:
        if n < 0:
            return 0
        now_cost = costs[n] if n < len(costs) else 0
        result = self.cache[n]
        if result == -1:
            result = now_cost + min(
                self.back_tracking(costs, n-1), 
                self.back_tracking(costs, n-2),
            )
            self.cache[n] = result
        return result

def test_climb_stairs_back_tracking(climbStairs, result, n):
    for i in range(n):
        assert(climbStairs.solution(i) == result[i])

def test_climb_stairs_dynamic_programming(climbStairs, result, n):
    for i in range(n):
        assert(climbStairs.solution(i, DYNAMIC_PROGRAMMING) == result[i])

def test_climb_stairs():
    result = [1, 1, 2, 3, 5, 8, 13, 21]
    climbStairs = ClimbingStairs()
    print("test_climb_stairs_back_tracking...")
    test_climb_stairs_back_tracking(climbStairs, result, len(result))
    print("susccess")
    print("test_climb_stairs_dynamic_programming...")
    test_climb_stairs_dynamic_programming(climbStairs, result, len(result))
    print("success")

def test_min_cost_climb_stairs_back_tracking(minCostClimbingStairs, test_cases):
    for t_case in test_cases:
        assert(minCostClimbingStairs.solution(t_case[0]) == t_case[1])

def test_min_cost_climb_stairs_dynamic_programming(minCostClimbingStairs, test_cases):
    for t_case in test_cases:
        assert(minCostClimbingStairs.solution(t_case[0], DYNAMIC_PROGRAMMING) == t_case[1])

def test_min_cost_climb_stairs():
    test_cases =[
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
        ([0, 0, 0, 0], 0),
        ([16, 19, 10, 12, 18], 31),
        ([2, 5, 3, 1, 7, 3, 4], 9),
        ([], 0),
        ([1], 0),
        ([1, 2], 1),
        ([2, 1], 1)
    ]

    minCostClimbingStairs = MinCostClimbingStairs()
    print("test_min_cost_climb_stairs_back_tracking...")
    test_min_cost_climb_stairs_back_tracking(minCostClimbingStairs, test_cases)
    print("susccess")
    print("test_min_cost_climb_stairs_dynamic_programming...")
    test_min_cost_climb_stairs_dynamic_programming(minCostClimbingStairs, test_cases)
    print("success")

if __name__ == "__main__":
    test_climb_stairs()
    test_min_cost_climb_stairs()
