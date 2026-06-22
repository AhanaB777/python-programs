class Node:
    def __init__(self,item):
        self.info=item
        self.left=None
        self.right=None
    
class BinaryTree:
    def __int__(self):
        self.left=None
        self.right=None
    
firstNode=Node(2)
secondNode=Node(3)
thirdNode=Node(4)
fourthNode=Node(5)

firstNode.left=secondNode
firstNode.right=thirdNode
secondNode.left=fourthNode