'''
Given the head of a linked list, return the node 
where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node 
in the list that can be reached again by continuously 
following the next pointer. Internally, pos is used to 
denote the index of the node that tail's next pointer is 
connected to (0-indexed). It is -1 if there is no cycle. 
Note that pos is not passed as a parameter.

Do not modify the linked list.

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, 
where tail connects to the second node. 
'''

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = q = head
        while p and q and q.next:
            p = p.next
            q = q.next.next
            if p == q:
                q = head
                while (p != q):
                    p = p.next
                    q = q.next
                return p                      
        return None

def main():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next = l1.next
    s = Solution()
    l = s.detectCycle(l1)
    while l:
        print(l.val, end=' ')
        l = l.next

if __name__ == '__main__':
    main()