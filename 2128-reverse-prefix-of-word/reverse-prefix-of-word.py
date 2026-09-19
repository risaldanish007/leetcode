class Solution(object):
    def reversePrefix(self, word, ch):
        for w in range(len(word)):
          if word[w] == ch:
            a = word[:w+1]
            a = a[::-1] + word[w+1:]
            return a
        return word