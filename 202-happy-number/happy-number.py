class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)

            total = 0
            for d in str(n):
                total += int(d) ** 2

            n = total

        return n == 1