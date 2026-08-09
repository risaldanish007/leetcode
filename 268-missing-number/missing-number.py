class Solution(object):
    def missingNumber(self, nums):
        Snum = set(nums)
        for i in range(len(nums)+1):    
            if i not in Snum:
                return i      