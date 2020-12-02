from collections import deque 
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        ret = []
        queue = deque()
        index = 0
        for i, n in enumerate(nums):
            # print i
            # print index
            # print queue
            if i >= k and i-k >= index:
                queue.popleft()
            while queue and queue[-1][1] <= n:
                queue.pop()
            queue.append((i, n))
            index = queue[0][0]
            if i >= k-1:
                ret.append(queue[0][1])
        return ret
        
    def test(self):
        nums = [1,3,-1,-3,5,3,6,7]
        # print self.maxSlidingWindow(nums, 3)
        # print self.maxSlidingWindow([1,-1], 1)
        # print self.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4)
        print self.maxSlidingWindow([1,-9,8,-6,6,4,0,5],4)
        # nums = []
        # print self.maxSlidingWindow(nums, 3)
        # nums = [1,3,-1]
        # print self.maxSlidingWindow(nums, 3)
        # nums = [1,3,-1,5]
        # print self.maxSlidingWindow(nums, 3)
        # nums = [1,3,-1,-3,5,3,6,7]
        # print self.maxSlidingWindow(nums, 2)
        # nums = [1,3,-1,-3,5,3,6,7]
        # print self.maxSlidingWindow(nums, 1)

if __name__ == "__main__":
    so = Solution()
    so.test()

    # nums = [1,2,4,2,1,3,10,22,11]
    # nums.sort()
    # print nums
    # x = (1,0)
    # print x[0]
    # import heapq
    # from Queue import PriorityQueue