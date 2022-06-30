from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        answer = []
        while stack or root is not None:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                answer.append(root.val)
                root = root.right    
        return answer    

def main():
    Tree_root = TreeNode(1)
    Tree_root.right = TreeNode(2)
    Tree_root.right.left = TreeNode(3)

    s = Solution()
    print(s.inorderTraversal(root=Tree_root))

if __name__ == '__main__':
    main()