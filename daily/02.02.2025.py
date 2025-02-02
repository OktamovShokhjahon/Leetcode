class Solution:
    def check(self, nums) -> bool:
        n = len(nums)
        for i in range(n):
            b = []
            for j in range(i, n):
                b.append(nums[j])
            for j in range(i):
                b.append(nums[j])
            a = True
            for j in range(n - 1):
                if b[j] > b[j + 1]:
                    a = False
                    break
            if a:
                return True
        return False