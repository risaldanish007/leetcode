class Solution(object):
    def areNumbersAscending(self, s):
        temp = 0
        for word in s.split():
            if word.isnumeric():
                num = int(word)
                
                if num<=temp:
                    return False
                temp = num
        return True