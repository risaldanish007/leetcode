import math
from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        count = len(nums)//2
        freq = Counter(nums)
        for i,j in freq.items():
            if j > count:
                return i