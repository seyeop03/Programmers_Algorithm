class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class CircularLinkedList:
    
    def __init__(self):
        self.tail = None
        self.count = 0
    
    def isEmpty(self):
        return self.count == 0
        
    def size(self):
        return self.count

    def insertHead(self,item):
        newNode = Node(item)
        if self.isEmpty():
            self.tail = newNode
            newNode.next = newNode
        else:
            newNode.next = self.tail.next
            self.tail.next = newNode
        self.count += 1

    def insertTail(self,item):
        newNode = Node(item)
        if self.isEmpty():
            self.tail = newNode
            newNode.next = newNode
        else:
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode # insertHead랑 이거 하나 차이임.
        self.count += 1
    
    
    def popAfter(self, prev):
        curr = prev.next
        Data = curr.data
        if self.count == 1:
            self.tail = None
        else:
            prev.next = curr.next
            self.tail = prev
        self.count -= 1
        return Data


    def print_list(self):
        if self.isEmpty():
            print('[]')
        else:
            first = self.tail.next
            curr = first
            while curr.next != first:
                print(curr.data, ' -> ', end='')
                curr = curr.next
            print(curr.data)