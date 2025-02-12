class Solution:
    def maximumSum(self, nums):
        dp = [-1] * 82
        mx = -1
        for i in nums:
            d = sum(int(d) for d in str(i))
            if dp[d] != -1:
                mx = max(mx, i + dp[d])
            dp[d] = max(dp[d], i)
        return mx