'''
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive 
elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        answer = 0
        for item in hashset:
            if item-1 not in hashset:
                num = item
                streak = 1

                while item+1 in hashset:
                    streak += 1
                    item += 1

                if answer < streak:
                    answer = streak
        return answer


                   

def main():
    s = Solution()
    r = [12, 4, 3, 11, 34, 35, 36, 1, 67]
    print(s.longestConsecutive(r))

if __name__ == '__main__':
    main()        