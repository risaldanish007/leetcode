from collections import Counter

class Solution(object):
    def findLucky(self, arr):
        freq = Counter(arr)
        ans = -1
        for i,j in freq.items():
            if i == j:
                ans = max(ans, i)
        return ans   
        