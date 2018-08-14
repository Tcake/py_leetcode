class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l_s = len(s)

        flag = 0
        start = 0
        finish = 0
        result = ''

        for i in range(l_s):
            if s[i] == '(':
                flag += 1
            else:
                flag -= 1

            if flag == 0:
                finish = i
                if finish - start + 1 > len(result):
                    result = s[start: finish + 1]
            elif flag < 0:
                start = i + 1
                flag = 0
        if flag > 0:
            if finish - start + 1 > len(result):
                result = s[start: finish + 1]

        return result


a = Solution()
test = '(()'
print(a.longestValidParentheses(test))