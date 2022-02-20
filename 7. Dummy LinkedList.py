##### insertAfter, popAfter을 추가 #####
### 위 두 메서드는 삽입/삭제하고자하는 노드의 전노드를 알면,
### O(1) 시간만에 삽입 및 삭제를 할 수 있다.
### 그리고 이 메서드를 추가하기 위해서
### Dummy Node가 필요하다 !!
### 이 두 메서드는 이전 노드를 이미 아는경우에 한해 효율적임.

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


    # 원소의 삽입(전 노드를 알고 있는 경우 연결만 바꾸기만 하면 됨)
    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        # prev(전 노드)가 tail일 경우/즉, 맨끝에 삽입할 경우 -> tail의 재정의 필요
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
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
            prev = self.getAt(pos - 1) # 6.연결리스트에서는 pos가 1일경우 getAt사용이 불가하여 pos가 1인경우를 따로 구현해줘야햇음
        return self.insertAfter(prev, newNode)


    # 원소의 삭제(삭제하는 노드의 data를 리턴)
    def popAfter(self, prev):
        curr = prev.next
        if curr is None:
            return None
        if curr.next is None:
            self.tail = prev
        prev.next = curr.next
        self.nodeCount -= 1
        return curr.data


    # popAfter 활용
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)


    def concat(self, L):
        self.tail.next = L.head.next
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount