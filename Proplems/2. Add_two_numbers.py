'''
You are given two non-empty linked lists representing 
two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def _get_fullnumber(self, l):
        def _recursive(l, number_of_zeros):
            if l.next is None:
                return l.val * 10**number_of_zeros
            return l.val * 10**number_of_zeros + _recursive(l.next, number_of_zeros + 1)

        if l is None:
            return 0
        return _recursive(l, 0)        

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = self._get_fullnumber(l1) + self._get_fullnumber(l2)
        totalstr = str(total)
        LastLN = ListNode(int(totalstr[0]))
        LN = None
        for i in range(1, len(totalstr)):
            LN = ListNode(int(totalstr[i]), LastLN)
            LastLN = LN
        if LN is None:
            return LastLN
        return LN


def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    s = Solution()
    print(s.addTwoNumbers(l1, l2))

if __name__ == '__main__':
    main()