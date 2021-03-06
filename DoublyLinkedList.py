### 일반적인 LinkedList의 경우 뒤로갈 수가 없다. 이러한 한계를 극복하기위해 양방향연결리스트를 구현한다.
### Dummy 를 맨처음(head), 맨끝(tail) 2개를 둔다. head, tail이 Dummy로서 고정되어 있으므로 따로 head,tail을 재조정한다거나 할 필요가 없다. 

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
    # 반으로 줄여서 탐색하기 위함(두동강내서 반이상이면 tail부터, 반이하면 head부터 )
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


    def insertBefore(self, next, newNode):
        prev = next.prev
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


    def popBefore(self, next):
        curr = next.prev
        prev = curr.prev
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data


    def popAt(self, pos):
        if pos < 1 or self.nodeCount < pos:
            raise IndexError
            
        prev = self.getAt(pos-1)
        return self.popAfter(prev)

    
    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount
