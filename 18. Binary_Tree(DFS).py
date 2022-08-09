class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    ###################### 이진트리 노드의 총 갯수 ######################
    # 전체 이진 트리의 size() ==  left subtree의 size() + right subtree의 size() + 1
    # 또 <left subtree>, <right subtree> 의 각 root가 있을테니 각 노드의 left subtree의 size() + right subtree의 size() + 1
    # ⋯ 계속 ⋯ (I'm gonna reduce it again and keep doing that until I get down to a simple case that I can solve directly.)
    # <추가> : L에서 l+r+1을 계산해서오고, R에서도 l+r+1을 계산해서 온다면, 호출한 Node를 포함한 갯수는 L+R+1이다
    # 즉, 자식 L,R을 부르고 -> 나중에 L, R 각각을 받고 -> L+R+1을 계산한 뒤 -> 최종적으로 L+R+1을 부모에게 돌려준다.
    def size(self):
        l = self.left.size() if self.left else 0 # 지금 노드(n)의 왼쪽 자식이 있으면 left.size() 호출
        r = self.right.size() if self.right else 0 # 지금 노드(n)의 오른쪽 자식이 있으면 right.size() 호출
        return l + r + 1

    # left subtree의 depth()와 right subtree의 depth()중 <더 큰 것 + 1>    
    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        if l > r:
            return l + 1
        else:
            return r + 1

    # Depth Breadth First의 중위순회(in-order)는 left subtree->자기자신->right subtree이다.
    def inorder(self):
        traversal = []
        if self.left: # left먼저
            traversal += self.left.inorder()
        traversal.append(self.data) # 그다음 자기자신 집어넣기
        if self.right: # 마지막 right
            traversal += self.right.inorder()
        return traversal

    # Depth Breadth First의 전위순회(pre-order)는 자기자신->left subtree->right subtree이다.
    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal
    
    # Depth Breadth First의 후위순회(post-order)는 left subtree->right subtree->자기자신 이다.
    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal


class BinaryTree:
    # 트리의 루트노드 지정
    def __init__(self, r):
        self.root = r
    
    
    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0
    
    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return 0

    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []
    
    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []