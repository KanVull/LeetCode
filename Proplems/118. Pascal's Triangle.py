'''
Given an integer numRows, return the first numRows 
of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers 
directly above it as shown:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: numRows = 1
Output: [[1]]
'''

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        if numRows < 2:
            return arr
        for _ in range(1, numRows):
            arr.append(
                [1] + [arr[-1][i]+arr[-1][i+1] for i in range(len(arr[-1])-1)] + [1]
            )
        return arr    
                   

def main():
    s = Solution()
    print(s.generate(6))

if __name__ == '__main__':
    main()        