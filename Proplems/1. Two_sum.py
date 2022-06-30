'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            if target - nums[i] in hash.keys():
                return [i, hash[target - nums[i]]]
            hash[nums[i]] = i

def main():
    nums = [2,7,11,15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))

if __name__ == '__main__':
    main()