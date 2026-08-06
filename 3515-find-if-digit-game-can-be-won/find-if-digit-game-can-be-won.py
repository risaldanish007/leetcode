class Solution(object):
    def canAliceWin(self, nums):
        sig = 0
        dub = 0
        
        for num in nums:
            if num < 10:
                sig+=num
            else:
                dub+=(num)
        
        return  sig != dub