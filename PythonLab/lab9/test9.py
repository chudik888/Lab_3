import unittest
from lab9 import TreeNode

class TestTreeNode(unittest.TestCase):
    def setUp(self):
        # Дерево для тестів
        self.tree_tuple = ((1, 3, None), 2, ((None, 3, 6), 5, (6, 7, 8)))
        self.root = TreeNode.create_tree(self.tree_tuple)

    def test_height(self):
        self.assertEqual(self.root.height(), 4)

    def test_size(self):
        self.assertEqual(self.root.size(), 9)

    def test_inorder_traversal(self):
        expected = [1, 3, 2, 3, 6, 5, 6, 7, 8]
        self.assertEqual(self.root.inorder_traversal(), expected)

    def test_preorder_traversal(self):
        expected = [2, 3, 1, 5, 3, 6, 7, 6, 8]
        self.assertEqual(self.root.preorder_traversal(), expected)

    def test_postorder_traversal(self):
        expected = [1, 3, 6, 3, 6, 8, 7, 5, 2]
        self.assertEqual(self.root.postorder_traversal(), expected)

if __name__ == '__main__':
    unittest.main()
