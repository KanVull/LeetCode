'''
Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using 
the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "ab"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

import collections
from typing import List

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cr = collections.Counter(ransomNote)
        cm = collections.Counter(magazine)
        return not cr - cm               


def main():
    s = Solution()
    print(s.canConstruct('aaff', 'ajgafakjr'))

if __name__ == '__main__':
    main()        