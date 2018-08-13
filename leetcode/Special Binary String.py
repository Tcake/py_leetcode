class Solution:
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = self.salve(S)
        return result

    def salve(self, item):
        if len(item) <= 4:
            return item

        flag = 0
        s_list = []
        front = 0
        for i in range(len(item)):
            if item[i] == '1':
                flag += 1
            else:
                flag -= 1

            if flag == 0:
                aft_item = '1' + self.salve(item[front + 1: i]) + '0'
                s_list.append(aft_item)
                front = i + 1

        res = ''
        while s_list:
            tmp = max(s_list)
            res += tmp
            s_list.remove(tmp)

        return res


a = Solution()
test = "11011000"
test1 = "1010101100"
print(a.makeLargestSpecial(test1))