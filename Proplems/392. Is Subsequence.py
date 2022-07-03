'''
Given two strings s and t, return true if s is a subsequence of t, 
or false otherwise.

A subsequence of a string is a new string that is formed 
from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions 
of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Input: s = "abc", t = "ahbgdc"
Output: true

Input: s = "axc", t = "ahbgdc"
Output: false
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True    
        index = 0
        for ch in t:
            if ch == s[index]:
                index += 1
                if index == len(s):
                    return True  
        return False             



def main():
    s = Solution()
    print(s.isSubsequence('b', 'abc'))

if __name__ == '__main__':
    main()        