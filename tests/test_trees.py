import pytest
from solutions.trees import TreeNode as TN, Trees


def test_invert_tree():

    tree0 = TN()
    tree1 = TN(0)
    tree2 = TN(2, TN(1), TN(3))
    tree3 = TN(4, TN(2, TN(1), TN(3)), TN(7, TN(6), TN(9)))

    assert Trees.invertTree(tree0) == TN()
    assert Trees.invertTree(tree1) == TN(0)
    assert Trees.invertTree(tree2) == TN(2, TN(3), TN(1))
    assert Trees.invertTree(tree3) == TN(4, TN(7, TN(9), TN(6)), TN(2, TN(3), TN(1)))
