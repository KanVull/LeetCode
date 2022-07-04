'''
There are n children standing in a line. Each child is assigned 
a rating value given in the integer array ratings.

You are giving candies to these children subjected to the 
following requirements:
 - Each child must have at least one candy.
 - Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute 
the candies to the children.

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, 
second and third child with 2, 1, 2 candies respectively.

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, 
second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
'''

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) < 2:
            return len(ratings)
        arr1 = [1] * len(ratings)
        arr2 = arr1.copy()
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                arr1[i] += arr1[i-1]
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i] < ratings[i-1]:
                arr2[i-1] += arr2[i]
            if arr2[i] < arr1[i]:
                arr2[i] = arr1[i]
        return sum(arr2)            

def main():
    s = Solution()
    r = [12, 4, 3, 11, 34, 34, 1, 67]
    print(s.candy(r))

if __name__ == '__main__':
    main()        