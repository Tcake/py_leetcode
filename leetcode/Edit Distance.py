class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 and not word2:
            return 0

        l_word1 = len(word1)
        l_word2 = len(word2)

        if l_word1 > l_word2:
            word1, word2 = word2, word1
            l_word1, l_word2 = l_word2, l_word1

