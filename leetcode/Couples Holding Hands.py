class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        row_len = len(row)
        count = 0
        i = 0
        while i < row_len:
            rowi_cache = row[i] // 2
            if rowi_cache != row[i + 1] // 2:
                for j in range(i+2, row_len):
                    if row[j] // 2 == rowi_cache:
                        if j % 2 == 0:
                            tmp = row[j+1]
                            row[j+1] = row[i]
                            row[i] = tmp
                        else:
                            tmp = row[j-1]
                            row[j-1] = row[i]
                            row[i] = tmp
                        count += 1
                        i -= 2
                        break
            i += 2
        return count


a = Solution()
test = [3, 1, 2, 0]
print(a.minSwapsCouples(test))
