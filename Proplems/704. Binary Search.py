'''
Given an array of integers nums which is sorted 
in ascending order, and an integer target, 
write a function to search target in nums. 
If target exists, then return its index. 
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if not nums[left] <= target <= nums[right]:
            return -1

        while left < right:
            middle = (left + right) // 2 + 1
            if target == nums[middle]:
                return middle
            if target > nums[middle]:
                left = middle
            else:
                right = middle - 1
        return left if nums[left] == target else -1            

def main():
    nums = [-2,1,3,4,6,8,10,13,14]
    s = Solution()
    print(s.search(nums, 6))

if __name__ == '__main__':
    main()        