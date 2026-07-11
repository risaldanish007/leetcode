class Solution(object):
    def shuffle(self, nums, n):
        listx = nums[:n]
        listy = nums[n:]
        res=[]
        for i in range(n):
            res.append(listx[i])
            res.append(listy[i])
        return res