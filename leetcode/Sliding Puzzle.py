from copy import deepcopy

class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        history = {str(board): True}
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    cache = {str(board): (i, j, board)}
        count = 0

        while cache:
            # print(cache)
            tmp = {}
            for key in cache.keys():
                i, j, model = cache[key]
                if model == [[1, 2, 3], [4, 5, 0]]:
                    return count
                if i == 0:
                    item = deepcopy(model)
                    item[i][j] = item[i + 1][j]
                    item[i + 1][j] = 0
                    if not history.get(str(item)):
                        history.update({str(item): True})
                        tmp.update({str(item): (i + 1, j, deepcopy(item))})
                if i == 1:
                    item = deepcopy(model)
                    item[i][j] = item[i - 1][j]
                    item[i - 1][j] = 0
                    if not history.get(str(item)):
                        history.update({str(item): True})
                        tmp.update({str(item): (i - 1, j, deepcopy(item))})

                if j == 0 or j == 1:
                    item = deepcopy(model)
                    item[i][j] = item[i][j + 1]
                    item[i][j + 1] = 0
                    if not history.get(str(item)):
                        history.update({str(item): True})
                        tmp.update({str(item): (i, j + 1, deepcopy(item))})

                if j == 2 or j == 1:
                    item = deepcopy(model)
                    item[i][j] = item[i][j - 1]
                    item[i][j - 1] = 0
                    if not history.get(str(item)):
                        history.update({str(item): True})
                        tmp.update({str(item): (i, j - 1, deepcopy(item))})

            cache = tmp
            # print(cache)
            count += 1

        return -1

        # print(cache)


a = Solution()
test = [[4,1,2],[5,0,3]]

test1 = [[3,0,1],[2,4,5]]

test2 = [[1,2,3],[5,4,0]]
print(a.slidingPuzzle(test1))
