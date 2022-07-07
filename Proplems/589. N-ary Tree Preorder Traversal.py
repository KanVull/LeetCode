'''
Given the root of an n-ary tree, 
return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level 
order traversal. Each group of children is separated by 
the null value

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
'''

from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: Node) -> List[int]:
        if not root:
            return []               
        stack = [root]
        answer = []
        while stack != []:
            node = stack.pop(0)
            answer.append(node.val)
            if node.children is not None:
                stack = node.children + stack
        return answer        


def main():
    n3 = Node(3)
    n5,n6 = Node(5), Node(6)
    n3.children = [n5,n6]
    n2, n4 = Node(2), Node(4)
    n1 = Node(1, [n3,n2,n4])
    s = Solution()
    print(s.preorder(n1))

if __name__ == '__main__':
    main()        