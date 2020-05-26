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

    # create binary tree, and insert new element
    def insert(self, node: Node, data: int):
        # if root is null, then create a new node to apply to the root element
        if self.root is None:
            self.root = Node(data=data)
        # if data is greater than the data of root, than we just should look at the part of right.
        elif data > node.data:
            # if node.right is null, set the right to be the new node.
            if node.right is None:
                node.right = Node(data=data)
            # else go on looking at the part of right
            else:
                self.insert(node.right, data)
        # if data is lesser than the data of root, than we just should look at the part of left.
        else:
            # if node.left is null, set the left to be the new node.
            if node.left is None:
                node.left = Node(data=data)
            # else go on looking at the part of left
            else:
                self.insert(node.left, data)

    # find the smallest element
    def find_minimum(self, root: Node) -> Node:
        current: Node = root
        # we just need to look at the leftmost element
        while current.left is not None:
            current = current.left
        return current

    # find the biggest element.
    def find_maximum(self, root: Node) -> Node:
        current: Node = root
        # we just need to look at the rightmost element.
        while current.right is not None:
            current = current.right
        return current

    # get the height of the tree. use recursion to get left and right
    def get_height(self, node: Node) -> int:
        if node is None:
            return 0
        else:
            left_height = self.findHeigh(node.left)
            right_height = self.findHeigh(node.right)
            # don't forget to add 1
            height = max(left_height, right_height) + 1
            return height

    # use queue to interate the elements
    def breadth_frist_traversal(self, root: Node):
        queue = []
        queue.append(root)
        while len(queue) != 0:
            # pop the first element
            vertex: Node = queue.pop(0)
            print(vertex.data)
            # push the left element into queue
            if vertex.left is not None:
                queue.append(vertex.left)
            # push the right element into queue
            if vertex.right is not None:
                queue.append(vertex.right)

    # use stack to interate the elements
    def deepth_frist_traversal(self, root: Node):
        stack = []
        stack.append(root)
        while len(stack) != 0:
            # pop the the top element
            vertex: Node = stack.pop()
            print(vertex.data)
            # push the right into queue
            if vertex.right is not None:
                stack.append(vertex.right)
            # push the left into queue
            if vertex.left is not None:
                stack.append(vertex.left)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(bst.root, 15)
    bst.insert(bst.root, 12)
    bst.insert(bst.root, 8)
    bst.insert(bst.root, 14)
    bst.insert(bst.root, 13)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 18)
    bst.insert(bst.root, 22)
    bst.insert(bst.root, 19)

    # minimum = bst.findMin(bst.root)
    # print(minimum.data)
    # maximum = bst.findMax(bst.root)
    # print(maximum.data)
    # height = bst.findHeigh(bst.root)
    # print(height)

    # bst.breadth_frist_traversal(bst.root)
    bst.deepth_frist_traversal(bst.root)