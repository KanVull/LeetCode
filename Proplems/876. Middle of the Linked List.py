'''
Given the head of a singly linked list, 
return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with 
values 3 and 4, we return the second one.
'''

from operator import index
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        need_nodes = all_nodes = head
        while all_nodes and all_nodes.next:
            need_nodes = need_nodes.next
            all_nodes = all_nodes.next.next
        return need_nodes                   


def main():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    s = Solution()
    l = s.middleNode(l1)
    while l:
        print(l.val, end=' ')
        l = l.next

if __name__ == '__main__':
    main()