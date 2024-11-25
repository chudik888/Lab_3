from typing import Optional, Self, Union


class TreeNode:
    def __init__(self, key: int) -> None:
        self.key: int = key
        # self.obj = obj
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None

    def height(self) -> int:
        if not self:
            return 0

        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self) -> int:
        if not self:
            return 0

        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def display(
            self,
            space: str = "\t",
            level: int = 0
    ) -> None:
        if not self:
            print(f"{space * level}∅")
            return

        if not self.left and not self.right:
            print(f"{space * level}{self.key}")
            return

        TreeNode.display(self.right, space, level + 1)
        print(f"{space * level}{self.key}")
        TreeNode.display(self.left, space, level + 1)

    @staticmethod
    def create_tree(data: Union[tuple, int, None]) -> Optional["TreeNode"]:
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.create_tree(data[0])
            node.right = TreeNode.create_tree(data[2])
            return node
        elif data is None:
            return None
        else:
            return TreeNode(data)

    def dump_tree(self) -> tuple | int | None: # Union[tuple, int, None])
        if not self:
            return None
        if not self.left and not self.right:
            return self.key

        return TreeNode.dump_tree(self.left), self.key, TreeNode.dump_tree(self.right)

    def inorder_traversal(self) -> list[int]:
        if not self:
            return []

        return TreeNode.inorder_traversal(self.left) + [self.key] + TreeNode.inorder_traversal(self.right)

    # ============================================================================================== #
    # ======================================== LAB 9 =============================================== #
    # ============================================================================================== #
    def preorder_traversal(self) -> list[int]:
        if not self:
          return []
        return [self.key] + TreeNode.preorder_traversal(self.left) + TreeNode.preorder_traversal(self.right)

    def postorder_traversal(self) -> list[int]:
        if not self:
          return []
        return TreeNode.postorder_traversal(self.left) + TreeNode.postorder_traversal(self.right) + [self.key]
    
if __name__ == '__main__':
    # (left_subtree, key {obj} , right_subtree)
    tree_tuple = ((1, 3, None), 2, ((None, 3, 6), 5, (6, 7, 8)))
    root = TreeNode.create_tree(tree_tuple)
    # print(root)
    # print(root.key) # 0
    # print(root.left.key, root.right.key) # 1
    # print(root.left.left.key, root.left.right, root.right.left.key, root.right.right.key) # 2
    root.display()
    print(f"Tree height: {root.height()}, Size: {root.size()}")
    assert tree_tuple == root.dump_tree()
    print(f"Inorder traversal: {root.inorder_traversal()}")
    print(f"Preorder traversal: {root.preorder_traversal()}")
    print(f"Postorder traversal: {root.postorder_traversal()}")