class Solution:
    def minOperations(self, nums, k) -> int:
        heapq.heapify(nums)

        c = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))

            c += 1

        return c