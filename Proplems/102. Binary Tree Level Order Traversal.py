'''
Given the root of a binary tree, return the level order traversal 
of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]
'''

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])            
            level = [child for n in level for child in (n.left, n.right) if child]
        return ans                   

                   

def main():
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3, None, n5)
    n2 = TreeNode(2, n4, None)
    n1 = TreeNode(1, n2, n3)
    s = Solution()
    print(s.levelOrder(n1))

if __name__ == '__main__':
    main()        