#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n_l = len(nums)
        if n_l < 3:
            return []
        ret = []
        i = 0
        while i < n_l-2:
            j = i+1
            k = n_l-1
            while j < k:
                sums = nums[i]+nums[j]+nums[k]
                if sums < 0:
                    j += 1
                elif sums == 0:
                    ret.append([nums[i], nums[j], nums[k]])
                    temp = nums[j]
                    while j < k and nums[j] == temp:
                        j += 1
                    temp = nums[k]
                    while j < k and nums[k] == temp:
                        k -= 1
                else:
                    k -= 1
            while i < n_l-2 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return ret

