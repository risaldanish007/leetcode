class Solution(object):
    def transformArray(self, nums):
        nums = [0 if num % 2 == 0 else 1 for num in nums]
        return sorted(nums)


s = Solution()
print(s.transformArray([4, 3, 2, 1]))