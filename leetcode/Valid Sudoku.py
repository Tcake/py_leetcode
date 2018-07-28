class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[] for i in range(9)]
        cols = [[] for i in range(9)]
        boxs = [[[] for i in range(3)] for j in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    if board[i][j] in rows[i]:
                        return False
                    else:
                        rows[i].append(board[i][j])
                    if board[i][j] in cols[j]:
                        return False
                    else:
                        cols[j].append(board[i][j])
                    if board[i][j] in boxs[i // 3][j // 3]:
                        return False
                    else:
                        boxs[i // 3][j // 3].append(board[i][j])
        return True


a = Solution()
test = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
test1 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(a.isValidSudoku(test1))
