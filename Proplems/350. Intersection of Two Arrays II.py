'''
Given two integer arrays nums1 and nums2, return an array of their 
intersection. Each element in the result must appear as many times 
as it shows in both arrays and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''

from typing import List
import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2): 
            return self.intersect(nums2, nums1)
        c = collections.Counter(nums1)
        answer = []
        for item in nums2:
            if c[item] != 0:
                c[item] -= 1
                answer.append(item)
        return answer        

def main():
    nums1 = [1, 2, 3, 5, 6, 3]
    nums2 = [2, 5, 5]
    s = Solution()
    print(s.intersect(nums1, nums2))

if __name__ == '__main__':
    main()        