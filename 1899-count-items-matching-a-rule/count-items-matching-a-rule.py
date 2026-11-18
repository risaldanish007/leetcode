class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        count = 0
        for i in items:
            if ruleKey == "color":
                if ruleValue == i[1]:
                    count += 1
            elif ruleKey == "type":
                if ruleValue == i[0]:
                    count += 1
            elif ruleKey == "name":
                if ruleValue == i[2]:
                    count += 1
        return count