'''
Given an integer array nums, find the contiguous subarray 
(containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        S = 0
        ans = -10001
        for item in nums:
            S += item
            ans = max(ans, S)
            if S < 0: S = 0
        return ans    



def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    print(s.maxSubArray(nums))

if __name__ == '__main__':
    main()        