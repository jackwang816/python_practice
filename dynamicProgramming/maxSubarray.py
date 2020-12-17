RECURSIVE = 'recursive'
BRUTE_FORCE = 'brute force'
KADANE = 'kadane'
class MaxSubarray(object):
    def __init__(self):
        self.solution_dict = {
            RECURSIVE: self._recursive,
            BRUTE_FORCE: self._brute_force,
            KADANE: self._dp_kadane,
        }

    def solution(self, nums: list, solution: str=RECURSIVE) -> int:
        return self.solution_dict[solution](nums, len(nums))

    def _recursive(self, nums: list, n: int) -> int:
        """ recursive sulotion
            max_sum = max(
                max(sums of all subarray ended with nums[n]), 
                recursive(n-1)
            )
            recursive(n-1) means maxsubarray from nums[0:n-1]
            Time Complexity: O(n^2)
        """
        if n==0:
            return 0
        if n==1:
            return nums[0]
        max_sum, idx = self._recursive(nums[0:n-1], n-1), n-1
        s = 0
        while idx >= 0:
            s += nums[idx]
            max_sum = max(s, max_sum)
            idx -= 1
        # print(n, max_sum)
        return max_sum

    def _brute_force(self, nums: list, n: int) -> int:
        """brute force solution
            Time Complexity: O(n^2)
        """
        max_sum = nums[0]
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                max_sum = max(s, max_sum)
        return max_sum

    def _dp_kadane(self, nums: list, n: int):
        """ Kadane's solution
            loop invariant: local_max(i) = max(nums[i], local_max(i-1) + nums[i])
                            global_max = max(local_max(0:i))
            definition of local_max(i): max subarray sums ended with nums[i]
            Time Complexity: O(n)
        """
        if n <= 0:
            return 0
        global_max = nums[0]
        local_max = 0
        for i in range(n):
            local_max = max(nums[i], local_max+nums[i])
            global_max = max(local_max, global_max)
        return global_max

if __name__ == "__main__":
    maxsubarray = MaxSubarray()
    test_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    n = len(test_list)
    # print(test_list[0:n-1])
    # print(n)
    # print(sum(test_list[0:1]))
    # print(sum(test_list[n-1:n]))
    # print(test_list[0:n])
    print(maxsubarray.solution(test_list))
    print(maxsubarray.solution(test_list, BRUTE_FORCE))
    print(maxsubarray.solution(test_list, KADANE))

