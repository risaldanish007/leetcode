from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        count = 0
        current = None
        
        for num in nums:
            if count == 0:
                current = num
            
            if num == current:
                count+=1
            else:
                count-=1
        
        return current