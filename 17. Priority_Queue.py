class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' -> '
        return s


    def getLength(self):
        return self.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)


    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail

        self.nodeCount += L.nodeCount

# 우선순위 큐는 내림자순으로 정렬되어 있다. ex) [10 , 9 , 5 , 3 , 1] 

class PriorityQueue:

    def __init__(self):
        self.queue = DoublyLinkedList()


    def size(self):
        return self.queue.getLength()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head
        # curr.next.next로 노드가 있는지 없는지 굳이 확인하는 이유는
        # 오직 실질적인 데이터만 가지고 비교연산을 하기 위함이다.
        # 만약 curr.next.next가 없고, 우선순위가 가장 높은 큐를 집어넣으려고 할 때
        # 결국에는 의미없는 tail과 비교를 하기때문에 반드시 비교할 구간을 정해주어야 한다.
        while curr.next.next and newNode.data < curr.next.data: 
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data