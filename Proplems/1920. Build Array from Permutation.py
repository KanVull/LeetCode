'''
Given a zero-based permutation nums (0-indexed), 
build an array ans of the same length where 
ans[i] = nums[nums[i]] 
for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers 
from 0 to nums.length - 1 (inclusive).
'''

class Solution:
    buildArray = lambda self, nums: \
                 [nums[item] for item in nums] 

def main():
    s = Solution()
    print(s.buildArray([0,2,1,4,5,3,2]))

if __name__ == '__main__':
    main()