'''
Write an efficient algorithm that searches for a value target 
in an m x n integer matrix matrix. This matrix has the following properties:
 - Integers in each row are sorted from left to right.
 - The first integer of each row is greater than the last integer 
   of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:    
        def search_row() -> int:
            up, down = 0, len(matrix) - 1
            while up < down:
                middle = (up + down) // 2 + 1
                if target == matrix[middle][0]:
                    return middle
                if target > matrix[middle][0]:
                    up = middle
                else:
                    down = middle - 1
            return up            


        def search_element_in_row(index):
            left, right = 0, len(matrix[0]) - 1
            if index == left and target < matrix[index][0] or index == right and target > matrix[index][-1]:
                return False
            while left < right:
                middle = (left + right) // 2 + 1
                if target == matrix[index][middle]:
                    return True
                if target > matrix[index][middle]:
                    left = middle
                else:
                    right = middle - 1
            return matrix[index][left] == target     

        return search_element_in_row(search_row())    
        


def main():
    nums = [[-2,1,3],[4,6,8],[10,13,14]]
    s = Solution()
    print(s.searchMatrix(nums, 7))

if __name__ == '__main__':
    main()        