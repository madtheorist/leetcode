from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return (
                self.val == other.val
                and self.left == other.left
                and self.right == other.right
            )
        raise TypeError(
            f"Cannot compare instance of {self.__class__.__name__} with {other.__class__.__name__}"
        )


class Trees:

    @classmethod
    def invertTree(cls, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        https://leetcode.com/problems/invert-binary-tree/
        invert binary tree (in place!)
        """
        if root:
            root.left, root.right = root.right, root.left
            root.left = cls.invertTree(root.left)
            root.right = cls.invertTree(root.right)
            return root
        
    @classmethod
    def maxDepth(cls, root: Optional[TreeNode]) -> int:
        """
        https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/1231564924/
        Max depth of binary tree - recursive dfs
        """
        if not root:
            return 0
        
        # recursive DFS
        return 1 + max(cls.maxDepth(root.left), cls.maxDepth(root.right))

        # alternative - iterative DFS
        stack = [[root, 1]]
        res = 1
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

        # alternative 2 - BFS, level-order traversal
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    @classmethod
    def diameterOfBinaryTree(cls, root: Optional[TreeNode]) -> int:
        """
        https://leetcode.com/problems/diameter-of-binary-tree/description/
        """
        pass