class Solution:
    def maxAscendingSum(self, nums) -> int:
        c = res = nums[0]
        for i in range(1, len(nums)):
            c = c + nums[i] if nums[i] > nums[i-1] else nums[i]
            res = max(res, c)
        return res