'''
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        braskets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = ''
        for ch in s:
            if ch in braskets.keys():
                if stack == '':
                    return False
                if stack[-1] != braskets[ch]:
                    return False
                else:
                    stack = stack[:-1]
            else:
                stack += ch
        return stack == ''                
                        

def main():
    st = '(()[[()]{}])'
    s = Solution()
    print(s.isValid(st))

if __name__ == '__main__':
    main()        