class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    # 이진트리 노드의 총 갯수
    # 전체 이진 트리의 size() ==  left subtree의 size() + right subtree의 size() + 1
    # 또 <left subtree>, <right subtree> 의 각 root가 있을테니 각 노드의 left subtree의 size() + right subtree의 size() + 1
    # ⋯ 계속 ⋯
    def size(self):
        l = self.left.size() if self.left else 0 # 지금 노드(n)의 왼쪽 자식이 있으면 left.size() 호출
        r = self.right.size() if self.right else 0 # 지금 노드(n)의 오른쪽 자식이 있으면 right.size() 호출
        return l + r + 1



class BinaryTree:
    # 트리의 루트노드 지정
    def __init__(self, r):
        self.root = r
    
    
    def size():
