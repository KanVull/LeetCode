'''
Given two strings s and t, return true if t is 
an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging 
the letters of a different word or phrase, typically 
using all the original letters exactly once.
'''

import collections
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs = collections.Counter(s)
        for ch in t:
            if ch in cs:
                cs[ch] -= 1
            else:
                return False    
        return not any(cs.values())           


def main():
    s = Solution()
    print(s.isAnagram('rat', 'car'))

if __name__ == '__main__':
    main()        