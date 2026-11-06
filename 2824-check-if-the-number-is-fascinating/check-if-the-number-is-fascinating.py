class Solution(object):
    def isFascinating(self, n):
        concat = str(n) + str(2 * n) + str(3 * n)
        return len(concat) == 9 and set(concat) == set("123456789")