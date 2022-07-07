class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        pass


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    # 인자: 찾으려는 대상 키 / Return: <찾은 노드> 및 찾은 노드의 <부모 노드>
    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None


    def min(self):
        if self.left:
            return self.left.min()
        else:
            return None

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return None

class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
    
    # 인자: 찾으려는 대상 키 / Return: <찾은 노드> 및 찾은 노드의 <부모 노드>
    def lookup(self,key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None


    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None

    def max(self):
        if self.root:
            return self.root.max()
        else:
            return None


def solution(x):
    return 0