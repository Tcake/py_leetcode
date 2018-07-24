class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]
        result_list = [0, 1]
        flag = 1.0
        index = 0
        for i in xrange(2, num + 1):
            if i / flag == 2:
                index = 0
                flag *= 2
                result_list.append(result_list[index] + 1)

            else:
                result_list.append(result_list[index] + 1)
            index += 1
        return result_list


a = Solution().countBits(10)
print(a)
