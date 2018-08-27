class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = ''
        result = 0
        for char in s:
            if char in tmp:
                if len(tmp) == 1:
                    continue
                else:
                    index = tmp.index(char)
                    tmp = tmp[index + 1:] + char
            else:
                tmp += char
                result = max(len(tmp), result)

        return result


a = Solution()
test = 'abcabcbb'
test1 = 'bbbbb'
test2 = 'pwwkew'
print(a.lengthOfLongestSubstring(test2))
