class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        cache = {}
        def slave(item):

            if not item:
                return ['']
            if item in cache:
                return cache[item]
            is_success = False
            result = []
            for word in wordDict:
                if item.startswith(word):
                    res = slave(item[len(word):])
                    if res:
                        is_success = True
                        for a_res in res:
                            if a_res == '':
                                result.append(word)
                            else:
                                result.append(word + ' ' + a_res)
            if not is_success:
                cache[item] = []
                return []
            else:
                cache[item] = result
                return result

        return slave(s)


a = Solution()
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
s1 = "catsanddog"
wordDict1 = ["cat", "cats", "and", "sand", "dog"]
s2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict2 = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(a.wordBreak(s2, wordDict2))