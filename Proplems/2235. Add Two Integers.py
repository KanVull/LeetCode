'''
Given two integers num1 and num2, return the sum of the two integers.

Input: num1 = -10, num2 = 4
Output: -6
Explanation: num1 + num2 = -6, so -6 is returned.
'''

class Solution:
    sum = lambda self, x,y: x+y   

def main():
    s = Solution()
    print(s.sum(3,4))

if __name__ == '__main__':
    main()