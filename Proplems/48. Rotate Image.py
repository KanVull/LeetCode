'''
You are given an n x n 2D matrix representing an image, 
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have 
to modify the input 2D matrix directly. DO NOT allocate another 
2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for y in range(len(matrix)):
            for x in range(y + 1, len(matrix)):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]           
        for y in range(len(matrix)):
            for x in range(len(matrix) // 2):
                matrix[y][x], matrix[y][-x - 1] = matrix[y][-x - 1], matrix[y][x]


def main():
    nums = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    s = Solution()
    s.rotate(nums)
    print(nums)

if __name__ == '__main__':
    main()        