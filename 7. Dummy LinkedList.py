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
        # head가 더미 노드이기 때문에
		# Dummy head바로 뒤인 next부터 읽기 시작한다.
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        # 범위 밖의 경우
        if pos < 0 or pos > self.nodeCount:
            raise IndexError

        # 시작이 head(더미 노드)이기 때문에 0부터 시작해도 된다.
        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr


    # 원소의 삽입(전 노드를 알고 있는 경우)
    def insertAfter(self, prev, newNode):
        curr = prev.next
        # prev(전 노드)가 tail일 경우 -> tail의 재정의 필요
        if curr is None:
            self.tail = newNode
        prev.next = newNode
        newNode.next = curr
        self.nodeCount += 1
        return True


    # insertAfter 활용
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            raise IndexError

        # prev가 tail인 경우 -> 노드를 탐색할 필요 없이 tail을 활용할 수 있다.
        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    # 원소의 삭제(삭제하는 노드의 data를 리턴)
    def popAfter(self, prev):
        curr = prev.next
        if curr is None:
            return None
        data = curr.data
        if curr.next is None:
            self.tail = prev
        prev.next = curr.next
        self.nodeCount -= 1
        return data


    # popAfter 활용
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)


    def concat(self, L):
        prev = self.tail
        next = self.head.next
        prev.next = next
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount