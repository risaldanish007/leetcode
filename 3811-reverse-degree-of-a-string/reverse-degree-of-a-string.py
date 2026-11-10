class Solution(object):
    def reverseDegree(self, s):
        total = 0

        for i, char in enumerate(s, 1):
            reverse_value = 26 - (ord(char) - ord('a'))
            total += reverse_value * i

        return total