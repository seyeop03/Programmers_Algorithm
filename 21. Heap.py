class MaxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        if len(self.data) == 1:
            self.data.append(item)
        else:
            cur = len(self.data)
            self.data.append(item)
            while cur != 0 and self.data[cur//2] < item:
                print('parent:',self.data[cur], 'item:',item)
                self.data[cur//2], self.data[cur] = self.data[cur], self.data[cur//2]
                cur //= 2
                break
heap = MaxHeap()
heap.insert(2)
heap.insert(4)
heap.insert(19)
heap.insert(24)
# heap.insert(12)
# heap.insert(18)
# heap.insert(21)
# heap.insert(30)
# heap.insert(6)
# heap.insert(8)

print(heap.data)