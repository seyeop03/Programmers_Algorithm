class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'
        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            raise IndexError

        if pos == 1: # 첫번째 인덱스에 삽입하는 경우는 그냥 head만 갈켜주면 된다. 그래서 이전 노드가 필요없다.
            newNode.next = self.head # 데이터를 처음으로 추가할 때도 이 코드로 커버 가능하다.
            self.head = newNode
 
        else: # 나머지 인덱스의 경우는 <이전노드의 링크도 바꿔야>하기 때문에 이전 노드가 필요하다.
            if pos == self.nodeCount + 1: # 끝에 추가할 경우엔
                prev = self.tail # 굳이 getAt사용할 필요 X
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1: # 맨끝에 추가할 경우는 특히 tail을 바꿔줌
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos < 1 or self.nodeCount < pos:
            raise IndexError
        if pos == 1: # 데이터가 1개일 때도 이 코드로 커버 가능하다. 그냥 None을 head로 놓는거니까
            curr = self.head
            self.head = curr.next # pop이니까 2번째 노드를 head로
            if pos == self.nodeCount:
                self.tail = None
        else:
            prev = self.getAt(pos-1)
            curr = prev.next
            prev.next = curr.next
            if pos == self.nodeCount:
                self.tail = prev
            self.nodeCount -= 1
        return curr.data


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0
