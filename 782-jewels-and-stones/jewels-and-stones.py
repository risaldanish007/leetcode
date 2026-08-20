class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        ss = set(jewels)
        j=0
        for i in stones:
            if i in ss:
                j+=1
        return j