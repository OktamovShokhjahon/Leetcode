class Solution:
    def countBadPairs(self, nums) -> int:
        c = 0
        d = {}
        for i in range(len(nums)):
            q = i - nums[i]
            g = d.get(q, 0)
            c += i - g
            d[q] = g + 1
        return c