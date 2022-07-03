'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s 
can be replaced to get t.

All occurrences of a character must be replaced 
with another character while preserving the order of characters. 
No two characters may map to the same character, 
but a character may map to itself.

Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "paper", t = "title"
Output: true
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        accS = {}
        accT = {}
        for i in range(len(s)):
            if s[i] in accS:
                if accS[s[i]] != t[i]:
                    return False    
            else:
                accS[s[i]] = t[i]
            if t[i] in accT:
                if accT[t[i]] != s[i]:
                    return False
            else:
                accT[t[i]] = s[i]
        return True              



def main():
    s = Solution()
    print(s.isIsomorphic('badc', 'baba'))

if __name__ == '__main__':
    main()        