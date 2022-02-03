# Dummy node가 있는 LinkedList

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    def traverse(self):
        result = []
        curr = self.head
        # head가 더미 노드이기 때문에 next를 활용할 수 있다.
        while curr.next:
            # head(더미노드)부터 시작했기 때문에 더미 노드가 없는 연결 리스트와 순서를 달리해야한다.
            curr = curr.next
            result.append(curr.data)
        return result