class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        self.s = s
        self.cache = [[-1] * l for _ in range(l)]
        r = 0
        tmp = ""
        for i in range(l):
            for j in range(i, l):
                res = self.slave(i, j)
                # print (res)
                if res > r:
                    r = res
                    tmp = s[i:j + 1]
        print(self.cache)
        return tmp

    def slave(self, i, j):
        if i == j:
            self.cache[i][j] = 1

        if self.cache[i][j] == -1:
            if self.s[i] == self.s[j]:
                if i - j == -1:
                    self.cache[i][j] = 2
                else:
                    res = self.slave(i + 1, j - 1)
                    if res > 0:
                        self.cache[i][j] = res + 2
                    else:
                        self.cache[i][j] = 0
            else:
                self.cache[i][j] = 0

        return self.cache[i][j]


a = "cccccccccc"
print(Solution().longestPalindrome(a))
