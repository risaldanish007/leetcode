class Solution(object):
    def findWordsContaining(self, words, x):
        countArr = []
        
        for i,word in enumerate(words):
            for char in word:
                if x == char:
                    countArr.append(i)
                    break
        return countArr
