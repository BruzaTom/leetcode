class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for t in range(0, len(nums)):
                if i != t:
                    if (nums[i] + nums[t]) == target:
                        return [i, t]