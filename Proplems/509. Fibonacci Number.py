'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the sum 
of the two preceding ones, starting from 0 and 1. That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
'''

class Solution:
    def fib(self, n: int) -> int:              
        f1, f2 = 0, 1
        if n < 1:
            return f1
        for i in range(1,n):
            f1, f2 = f2, f2+f1
        return f2         


def main():
    s = Solution()
    print(s.fib(4))

if __name__ == '__main__':
    main()        