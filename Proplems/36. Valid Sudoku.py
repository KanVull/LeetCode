'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the 
digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left 
corner being modified to 8. Since there are two 8's in the top left 
3x3 sub-box, it is invalid.
'''

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:   
        def is_valid(line):
            check = [item for item in line if item != '.']
            return len(check) == len(set(check))

        for row in board:
            if not is_valid(row):
                return False
        for col in zip(*board):
            if not is_valid(col):
                return False
        for i in (0,3,6):
            for j in (0,3,6):
                line = []
                for k in range(3):
                    line.extend(board[i+k][j:j+3])
                if not is_valid(line):
                    return False
        return True                              

def main():
    board = [
        [".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]
    ]
    s = Solution()
    print(s.isValidSudoku(board))

if __name__ == '__main__':
    main()        