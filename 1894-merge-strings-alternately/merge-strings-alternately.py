class Solution(object):
    def mergeAlternately(self, word1, word2):
        loop = max(len(word1),len(word2))
        merged = []
        len1 = len(word1)
        len2 = len(word2)
        for i in range(loop):
            if len1>i:
                merged.append(word1[i])
            if len2>i:
                merged.append(word2[i])
            
        return "".join(merged)