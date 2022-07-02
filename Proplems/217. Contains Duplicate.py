'''
Given an integer array nums, return true if any value 
appears at least twice in the array, 
and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


def main():
    nums = [121, 1, 555, 555, 111020111]
    s = Solution()
    print(s.containsDuplicate(nums))

if __name__ == '__main__':
    main()        