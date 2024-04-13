from typing import Optional


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
