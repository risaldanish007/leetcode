class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        counted = set()
        result = 0
        for i in range(len(word)):
            for x in range(len(word)):
                if (
                    word[i].islower()
                    and word[x].isupper()
                    and word[i].upper() == word[x]
                    ):
                    if word[i].lower() not in counted:
                        result += 1
                        counted.add(word[i].lower())
                        break
        return result