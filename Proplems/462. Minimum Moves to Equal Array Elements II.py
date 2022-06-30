'''
Given an integer array nums of size n, 
return the minimum number of moves required 
to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Input: nums = [1,10,2,9]
Output: 16
'''

from typing import List
import statistics

class Solution:
    def minMoves2(self, nums: List[int]) -> int: 
        if len(nums) == 1:
            return 0
        avg = round(statistics.median(nums))
        output = 0
        for num in nums:
            output += avg-num if avg-num > 0 else num-avg
        return output    


def main():
    nums = [1, 0, 0, 8, 6]
    s = Solution()
    print(s.minMoves2(nums))

if __name__ == '__main__':
    main()        