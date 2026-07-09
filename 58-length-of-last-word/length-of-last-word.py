class Solution(object):
    def lengthOfLastWord(self, s):
        alist = s.split()
        return len(alist[-1])