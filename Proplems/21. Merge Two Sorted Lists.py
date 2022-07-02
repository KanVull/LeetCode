'''
You are given the heads of two sorted linked lists 
list1 and list2.

Merge the two lists in a one sorted list. 
The list should be made by splicing together 
the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
'''
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2 
        if list2 is None: 
            return list1 
        l = []
        while list1 or list2: 
            if list1 is None: 
                l.append(list2.val) 
                list2 = list2.next 
                continue 
            if list2 is None: 
                l.append(list1.val) 
                list1 = list1.next 
                continue 
            if list1.val <= list2.val: 
                l.append(list1.val)
                list1 = list1.next 
            else: 
                l.append(list2.val) 
                list2 = list2.next  
        head = ListNode(l[-1])
        for item in l[:-1][::-1]:
            head = ListNode(item, head) 
        return head


def main():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    s = Solution()
    l = s.mergeTwoLists(l1, l2)
    while l:
        print(l.val, end=' ')
        l = l.next

if __name__ == '__main__':
    main()