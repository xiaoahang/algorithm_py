class Node(object):
    """
    docstring
    """

    def __init__(self, elem=-1, left=None, right=None):
        """
        docstring
        """
        self.elem = elem
        self.left = left
        self.right = right


class Tree(object):
    """
    docstring
    """

    def __init__(self):
        """
        docstring
        """
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        """
        docstring
        """
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue.append(treeNode.left)
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.myQueue.pop(0)

    def front_traverse(self, root):
        """
        docstring
        """
        if root == None:
            return
        print(root.elem)
        self.front_traverse(root.left)
        self.front_traverse(root.right)

    def middle_traverse(self, root):
        """
        docstring
        """
        if root == None:
            return
        self.front_traverse(root.left)
        print(root.elem)
        self.front_traverse(root.right)

    def later_traverse(self, root):
        """
        docstring
        """
        if root == None:
            return
        self.front_traverse(root.left)
        self.front_traverse(root.right)
        print(root.elem)

    def level_traverse(self, root):
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem)
            if node.left != None:
                myQueue.append(node.left)
            if node.right != None:
                myQueue.append(node.right)
