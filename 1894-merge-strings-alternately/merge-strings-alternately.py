class Solution(object):
    def mergeAlternately(self, word1, word2):
        loop = max(len(word1),len(word2))
        merged = ""
        
        for i in range(loop):
            if len(word1)>i:
                merged+=(word1[i])
            if len(word2)>i:
                merged+=(word2[i])
            
        return merged