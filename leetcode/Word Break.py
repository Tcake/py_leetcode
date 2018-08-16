class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        cache = {}
        # wordDict = sorted(wordDict, key=lambda x: len(x), reverse=True)
        def slave(item):
            if not item:
                return True
            if item in cache:
                return cache[item]
            for word in wordDict:
                if item.startswith(word):
                    res = slave(item[len(word):])
                    if res:
                        cache[item] = True
                        return True
            cache[item] = False
            return False

        return slave(s)

a = Solution()
s = "applepenapple"
wordDict = ["apple", "pen"]
s1 = "catsandog"
wordDict1 = ["cats","dog","sand","and","cat"]
s2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict2 = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(a.wordBreak(s2, wordDict2))