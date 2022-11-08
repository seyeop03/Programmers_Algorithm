from collections import deque
# 골드1 최솟값 찾기
class MaxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        if len(self.data) == 1:
            self.data.append(item)
        else:
            cur = len(self.data)
            self.data.append(item)
            while cur != 0 and self.data[cur//2] > item:
                self.data[cur//2], self.data[cur] = self.data[cur], self.data[cur//2]
                cur //= 2
                if cur == 1:
                    break

    def maxHeapify(self, i):
        left = 2*i
        right = 2*i + 1
        smallest = i
        
        if len(self.data)-1 >= left and self.data[smallest] >= self.data[left]:
            smallest = left

        if len(self.data)-1 >= right and self.data[smallest] >= self.data[right]:
            smallest = right

        if smallest != i:
            self.data[smallest], self.data[i] = self.data[i], self.data[smallest]
            self.maxHeapify(smallest)      

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data


N, L = map(int, input().split())

l = list(map(int, input().split()))
heap = MaxHeap()
d = deque()
idx = 0
cnt = {}

mini = l[0]

while idx < L:
    if l[idx] in cnt:    
        cnt[l[idx]] += 1 # count
    else:
        cnt[l[idx]] = 1
        heap.insert(l[idx])
        
    d.appendleft(l[idx])
    idx += 1
    if heap.data[1] >= mini:
        print(mini, end=' ')
    else:
        mini = heap.data[1]
        print(mini, end=' ')



for idx in range(L, N):
    d.appendleft(l[idx])
    if l[idx] in cnt:
        if cnt[l[idx]] == 0:
            heap.insert(l[idx])
        cnt[l[idx]] += 1
    else:
        cnt[l[idx]] = 1
        heap.insert(l[idx])
    
    prev = d.pop()
    cnt[prev] -= 1
    
    
    while cnt[heap.data[1]] == 0:
        heap.remove()
    
    mini = heap.data[1]

    print(mini, end=' ')