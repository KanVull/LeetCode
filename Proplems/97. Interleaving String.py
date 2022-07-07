'''
Given strings s1, s2, and s3, find whether s3 is formed 
by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration 
where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... 
                 or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Input: s1 = "", s2 = "", s3 = ""
Output: true
'''

from typing import List

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [False] * (len(s2) + 1)
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        return dp[len(s2)]                 
                      


def main():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    s = Solution()
    print(s.isInterleave(s1, s2, s3))

if __name__ == '__main__':
    main()        