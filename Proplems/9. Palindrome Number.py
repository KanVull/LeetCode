'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

Example:
121 is a palindrome while 123 is not.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for i in range(int(len(s)/2)):
            if s[i] != s[-i-1]:
                return False
        return True  

def main():
    nums = [121, 1, 555, 556, 111020111]
    s = Solution()
    print([(s.isPalindrome(num), num) for num in nums])

if __name__ == '__main__':
    main()        