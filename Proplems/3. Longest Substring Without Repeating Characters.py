'''
Given a string s, find the length of the longest substring 
without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, 
"pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or s == '':
            return 0
        s += s[-1]    
        maxLen = 1
        begIndex = 0
        for index, value in enumerate(s[1:]):
            try:
                i = s[begIndex : index+1].index(value)
                if maxLen < index + 1 - begIndex:
                    maxLen = index + 1 - begIndex
                begIndex += i+1
            except ValueError:
                continue
        return maxLen    


def main():
    st = ['abcabcbb', 'bbbbb', 'pwwkeq']
    s = Solution()
    print([(s.lengthOfLongestSubstring(ch), ch) for ch in st])

if __name__ == '__main__':
    main()