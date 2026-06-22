class Node:
    def __init__(self, item):
        self.info = item
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, item):
        if root is None:
            return Node(item)

        if item < root.info:
            root.left = self.insert(root.left, item)

        elif item > root.info:
            root.right = self.insert(root.right, item)

        return root

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.info, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(root.info, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.info, end=" ")

    def minValueNode(self, node):
        temp = node
        while temp.left is not None:
            temp = temp.left
        return temp

    def delete(self, root, item):
        if root is None:
            return root
        if item < root.info:
            root.left = self.delete(root.left, item)
        elif item > root.info:
            root.right = self.delete(root.right, item)
        else:
            if root.left is None:
                temp = root.right
                return temp
            elif root.right is None:
                temp = root.left
                return temp
            temp = self.minValueNode(root.right)
            root.info = temp.info
            root.right = self.delete(root.right, temp.info)
        return root

bst = BST()

bst.root = bst.insert(bst.root, 50)
bst.root = bst.insert(bst.root, 30)
bst.root = bst.insert(bst.root, 70)
bst.root = bst.insert(bst.root, 20)
bst.root = bst.insert(bst.root, 40)
bst.root = bst.insert(bst.root, 60)
bst.root = bst.insert(bst.root, 80)

print("Inorder:")
bst.inorder(bst.root)

print("\nPreorder:")
bst.preorder(bst.root)

print("\nPostorder:")
bst.postorder(bst.root)

bst.root = bst.delete(bst.root, 50)

print("\nAfter Deletion:")
bst.inorder(bst.root)