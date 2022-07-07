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

import collections
from typing import List

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = collections.Counter(s)
        for i, ch in enumerate(s):
            if c[ch] == 1:
                return i
        return -1       


def main():
    s = Solution()
    print(s.firstUniqChar('leetlcode'))

if __name__ == '__main__':
    main()        