class Solution(object):
    def minimumChairs(self, s):
        current = 0
        maximum = 0
        for i in range(len(s)):
            if s[i] == "E":
                current +=1
                maximum = max(current,maximum)
            else:
                current-=1
        return maximum
        