'''
The string "PAYPALISHIRING" is written in a zigzag pattern 
on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Example:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        index = 0
        addition = 1
        ch_dict = {i: '' for i in range(numRows)}
        for ch in s:
            ch_dict[index] += ch
            if index == numRows - 1 and addition == 1 or index == 0 and addition == -1:
                addition *= -1
            index += addition
        return ''.join(ch_dict.values())  

def main():
    st = 'PAYPALISHIRING'
    s = Solution()
    print(s.convert(st, 3))

if __name__ == '__main__':
    main()        