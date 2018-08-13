from copy import deepcopy

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        results = []
        res = []

        q_index = []

        def vaild(q_map, i, j):
            if q_map:
                for qi, qj in q_map:
                    if i == qi or j == qj:
                        return False
                    if (qi - i) / (qj - j) in (1, -1):
                        return False

            return True

        def salve(q_map, i, j):
            if vaild(q_map, i, j):
                if i == n - 1:
                    tmp = deepcopy(q_map)
                    tmp.append([i, j])
                    res.append(tmp)
                    return
                else:
                    q_map.append([i, j])
                    salve(q_map, i + 1, 0)
                    q_map.remove([i, j])
            if j < n - 1:
                salve(q_map, i, j + 1)

        salve(q_index, 0, 0)

        for answer in res:
            result = []
            for i, j in answer:
                result.append('.' * j + 'Q' + '.' * (n - 1 - j))
            results.append(result)
        return results


a = Solution()
print(a.solveNQueens(3))

# class Solution:
#     def __init__(self):
#         # self.sum = 0
#         self.upperlim = 1
#         self.result = []
#         self.output_queen=[]
#
#     def solveNQueens(self, n):
#         """
#         :type n: int
#         :rtype: List[List[str]]
#         """
#         self.upperlim = (1 << n) - 1
#         self.queen(0, 0, 0)
#         return self.output_queen
#
#     def queen(self, row, ld, rd):
#         if row != self.upperlim:
#             pos = self.upperlim & ~(row | ld | rd)
#             while pos:
#                 # p = pos & -pos
#                 p = pos & (~pos + 1)
#                 pos -= p
#                 self.result.append(p)
#                 self.queen(row + p, (ld + p) << 1, (rd + p) >> 1)
#                 self.result.pop()
#         else:
#             # self.sum += 1
#             self.print_queen()
#
#     def print_queen(self):
#         le = len(self.result)
#         out = []
#         for i in range(le):
#             tmp = self.result[i]
#             # print(bin(tmp))
#             count = 0
#             while(tmp != 0):
#                 tmp = tmp >> 1
#                 count += 1
#             out.append("."*(le-count) + "Q" + "."*(count-1))
#         self.output_queen.append(out)
