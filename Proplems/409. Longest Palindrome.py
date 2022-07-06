'''
Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
'''

from typing import List
import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:   
        count = collections.Counter(s)
        ret = 0
        for value in count.values():
            ret += value if value%2==0 else value-1
            if (value%2 == 1 and ret%2 == 0):
                ret += 1
        return ret        

def main():
    s = Solution()
    print(s.longestPalindrome("abccccdd"))

if __name__ == '__main__':
    main()        