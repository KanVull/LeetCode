'''
You are given a rectangular cake of size h x w and 
two arrays of integers horizontalCuts and verticalCuts where:

    - horizontalCuts[i] is the distance from the top of 
    the rectangular cake to the ith horizontal cut and similarly, 
and
    - verticalCuts[j] is the distance from the left of 
    the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after 
you cut at each horizontal and vertical position 
provided in the arrays horizontalCuts and verticalCuts. 
Since the answer can be a large number, return this modulo 
10^9 + 7.

Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. 
Red lines are the horizontal and vertical cuts. 
After you cut the cake, the green piece of cake has the maximum area.

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
'''

from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts += [0, h]
        verticalCuts += [0, w]
        horizontalCuts.sort()
        verticalCuts.sort()
        maximumH = 0
        maximumV = 0
        for i in range(len(horizontalCuts) - 1):
            new = horizontalCuts[i+1] - horizontalCuts[i]
            if maximumH < new:
                maximumH = new
        for i in range(len(verticalCuts) - 1):
            new = verticalCuts[i+1] - verticalCuts[i]
            if maximumV < new:
                maximumV = new
        return (maximumV * maximumH) % (10**9 + 7)                


def main():
    s = Solution()
    print( s.maxArea(5, 4, [4,2,1], [1,3]) )

if __name__ == '__main__':
    main()        