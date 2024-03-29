class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    # 트리에 주어진 데이터 원소를 추가
    def insert(self, key, data):
        # 인자: key, data
        # 리턴: 없음
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError('Key %s already exists.' % key)


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    # 특정 원소를 검색
    def lookup(self, key, parent=None):
        # 인자: 찾으려는 대상 키
        # 리턴 2개: <찾은 노드> 및 찾은 노드의 <부모 노드>
        # <부모 노드>는 remove에서 쓰이므로 이또한 리턴시켜줌.
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
        else:
            return self, parent

    # 특정 노드가 몇개자식을 가지는지
    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    # 최솟값: 그냥 왼쪽만 쭉 따라가면 됨
    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

    # 최댓값: 그냥 오른쪽만 쭉 따라가면 됨
    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self




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
    

    def lookup(self,key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None


    def remove(self, key):
        node, parent = self.lookup(key) # 일단, key로 node를 찾는다.(부모도)
        if node:
            nChildren = node.countChildren()
            # 1. 자식 0인 경우(The simplest case of no children)
            if nChildren == 0:
                # (1) parent가 있으면: 삭제하려는 node가 왼쪽 자식이었는지/오른쪽 자식이었는지를 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여 leaf node 였던 자식을 트리에서 없앰
                if parent:
                    if parent.key > node.key:
                        parent.left = None 
                    elif parent.key < node.key:
                        parent.right = None 
                # (2) parent가 없으면 node가 root라는 의미이므로,
                # self.root 를 None 으로 하여 빈 트리로 만듬
                else:
                    self.root = None
            # 2. 자식 1인 경우(When the node has only one child)
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여 그 자식을 어떤 변수가 가리키도록 함.
                if node.left:
                    tmp_node = node.left
                else:
                    tmp_node = node.right
                # 만약 parent가 있으면 node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣음.
                if parent:
                    if parent.key > node.key:
                        parent.left = tmp_node
                    elif parent.key < node.key:
                        parent.right = tmp_node 
                # 만약 parent가 없으면 node가 root라는 의미이므로,
                # self.root 에 위에서 가리킨 자식을 대신 넣음.
                else:
                    self.root = tmp_node
            # 3. 자식이 2인 경우(When the node has both left and right children)
            # 오른쪽 subtree의 최솟값으로 대체. 그리고 successor의 자식처리.
            else:
                parent = node # node는 삭제할 노드를 의미
                successor = node.right
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냄.
                while successor.left:
                    parent = successor
                    successor = successor.left
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입
                node.key = successor.key
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를 successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 함.
                ### 아래 모두 successor의 오른쪽 자식만을 가리키도록 함.
                if parent.right == successor: # successor가 root의 right인 경우
                    parent.right = successor.right
                elif successor == parent.left: # 오른쪽subtree에서 좌측으로 진행한 경우
                    parent.left = successor.right

            return True

        else:
            return False


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