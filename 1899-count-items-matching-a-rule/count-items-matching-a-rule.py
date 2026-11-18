class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        index = {"type":0,"color":1,"name":2}[ruleKey]
        count = 0

        for i in items:
            if i[index] == ruleValue:
                count+=1
        return count