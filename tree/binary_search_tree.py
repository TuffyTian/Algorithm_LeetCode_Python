"""
 * @Author: TuffyTian 
 * @Date: 2020-05-24 14:28:34 
 * @Last Modified by:   TuffyTian 
 * @Last Modified time: 2020-05-24 14:28:34 
"""


class Node:
    left = None
    right = None
    data = 0

    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, node: Node, data: int):
        if self.root is None:
            self.root = Node(data=data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data=data)
            else:
                self.insert(node.right, data)
        else:
            if node.left is None:
                node.left = Node(data=data)
            else:
                self.insert(node.left, data)

    def findMin(self, root: Node) -> Node:
        current: Node = root
        while current.left is not None:
            current = current.left
        return current

    def findMax(self, root: Node) -> Node:
        current: Node = root
        while current.right is not None:
            current = current.right
        return current

    def findHeigh(self, node: Node) -> int:
        if node is None:
            return 0
        else:
            left_height = self.findHeigh(node.left)
            right_height = self.findHeigh(node.right)
            height = max(left_height, right_height) + 1
            return height


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(bst.root, 15)
    bst.insert(bst.root, 8)
    bst.insert(bst.root, 17)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 25)
    bst.insert(bst.root, 12)
    bst.insert(bst.root, 6)

    minimum = bst.findMin(bst.root)
    print(minimum.data)
    maximum = bst.findMax(bst.root)
    print(maximum.data)
    height = bst.findHeigh(bst.root)
    print(height)
