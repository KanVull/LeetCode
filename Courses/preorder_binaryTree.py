from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root] if root is not None else []
        answer = []
        while stack:
            node = stack.pop() 
            answer.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return answer    

def main():
    Tree_root = TreeNode(1)
    Tree_root.right = TreeNode(2)
    Tree_root.right.left = TreeNode(3)

    s = Solution()
    print(s.preorderTraversal(root=Tree_root))

if __name__ == '__main__':
    main()