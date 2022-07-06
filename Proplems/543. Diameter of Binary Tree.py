'''
Given the root of a binary tree, 
return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path 
between any two nodes in a tree. This path may or may not pass 
through the root.

The length of a path between two nodes is represented by the 
number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Input: root = [1,2]
Output: 1
'''

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def depth(node):
            if node is None: return 0
            left, right = depth(node.left), depth(node.right)
            self.ans = max(self.ans, left+right)
            return 1 + max(left, right)
        depth(root)    
        return self.ans

def main():
    Tree_root = TreeNode(1)
    Tree_root.left = TreeNode(2)
    Tree_root.left.left = TreeNode(4)
    Tree_root.left.right = TreeNode(5)
    Tree_root.right = TreeNode(3)

    s = Solution()
    print(s.diameterOfBinaryTree(root=Tree_root))

if __name__ == '__main__':
    main()