import pytest
from solutions.trees import TreeNode as TN, Trees

tree0 = TN()
tree1 = TN(0)
tree2 = TN(2, TN(1), TN(3))
tree3 = TN(4, TN(2, TN(1), TN(3)), TN(7, TN(6), TN(9)))
tree4 = TN(3, TN(9), TN(20, TN(15), TN(7)))

@pytest.mark.parametrize(
    "tree, inverted_tree",
    [
        (tree0, TN()), 
        (tree1, TN(0)), 
        (tree2, TN(2, TN(3), TN(1))),
        (tree3, TN(4, TN(7, TN(9), TN(6)), TN(2, TN(3), TN(1))))
    ],
)
def test_invert_tree(tree, inverted_tree):
    assert Trees.invertTree(tree) == inverted_tree

@pytest.mark.parametrize(
    "tree, depth",
    [
        (tree0, 1), 
        (tree1, 1),
        (tree2, 2),
        (tree3, 3), 
        (tree4, 3)
    ],
)
def test_max_depth(tree, depth):
    assert Trees.maxDepth(tree) == depth