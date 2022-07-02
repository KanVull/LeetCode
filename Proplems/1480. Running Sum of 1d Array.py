'''
Given an array nums. We define 
a running sum of an array as 
runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: 
    [1, 1+2, 1+2+3, 1+2+3+4].

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: 
    [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
'''
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums        


def main():
    nums = [2,7,11,15]
    s = Solution()
    print(s.runningSum(nums))

if __name__ == '__main__':
    main()