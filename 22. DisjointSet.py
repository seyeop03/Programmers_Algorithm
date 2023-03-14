class DisjointSet: # 분리집합
    def __init__(self, item):
        self.parent = None
        self.data = item

    # 합집합
    def unionSet(self, Set):
        Set.findSet().parent = self.findSet()
    
    # 집합 탐색
    def findSet(self):
        node = self
        while node.parent is not None: # parent가 None인 노드는 root밖에 없다!
            node = node.parent
        return node
    
    def destroySet(self):
        del self

# 새로운 집합 생성
set1 = DisjointSet(1)
set2 = DisjointSet(2)

# 집합 합치기
set1.unionSet(set2)

# 루트 노드 확인
root_node = set1.findSet()
print(root_node.data)  # 1