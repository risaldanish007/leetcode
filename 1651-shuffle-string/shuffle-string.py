class Solution(object):
    def restoreString(self, s, indices):
        cs = ['']*len(s)
        for i,char in enumerate(s):
            cs[indices[i]] = char
        return "".join(cs)