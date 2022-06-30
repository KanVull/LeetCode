'''
Given a string of English letters s, 
return the greatest English letter 
which occurs as both a lowercase and uppercase letter in s. 
The returned letter should be in uppercase. 
If no such letter exists, return an empty string.

An English letter b is greater than another letter a 
if b appears after a in the English alphabet.

Example:
Input: s = "arRAzFif"
Output: "R"
Explanation:
The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, 
but 'R' is greater than 'F' or 'A'.

'''
from typing import List, Optional
import string

class Solution:
    def greatestLetter(self, s: str) -> str:
        hash = dict.fromkeys(string.ascii_lowercase, '')
        greatest = ''
        for ch in s:
            c = hash[ch.lower()] 
            if c == '':
                hash[ch.lower()] = ch
            else:
                if len(c) == 2:
                    continue
                if c[0] == ch:
                    continue
                else:
                    hash[ch.lower()] += ch
                    if ch.upper() > greatest:
                        greatest = ch.upper()
        return greatest                


def main():
    st = "arRAzFif"
    s = Solution()
    print(s.greatestLetter(st))

if __name__ == '__main__':
    main()