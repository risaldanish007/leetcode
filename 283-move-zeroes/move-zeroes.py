class Solution(object):
    def moveZeroes(self, nums):
        point = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[point],nums[i] = nums[i],nums[point]
                point+=1
        return nums