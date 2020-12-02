import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k_heap = []
        self.k = k
        for i, x in enumerate(nums):
            if i < k:
                heapq.heappush(self.k_heap, x)
            elif self.k_heap[0] < x:
                heapq.heappop(self.k_heap)
                heapq.heappush(self.k_heap, x)
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.k_heap) < self.k:
            heapq.heappush(self.k_heap, val)
            return self.k_heap[0]
        if val > self.k_heap[0]:
            heapq.heappop(self.k_heap)
            heapq.heappush(self.k_heap, val)
        return self.k_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
