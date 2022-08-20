class MaxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        # 데이터가 없다면 그냥 넣기.
        if len(self.data) == 1:
            self.data.append(item)
        # 데이터가 있다면, 일단 맨마지막에 넣고 부모와 계속 비교해서 교체
        else:
            cur = len(self.data)
            self.data.append(item)
            while cur != 0 and self.data[cur//2] < item:
                self.data[cur//2], self.data[cur] = self.data[cur], self.data[cur//2]
                cur //= 2
                break

    def maxHeapify(self, i):
        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left = 2*i

        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right = 2*i + 1

        smallest = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if len(self.data)-1 >= left and self.data[smallest] <= self.data[left]:
            # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.
            smallest = left

        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if len(self.data)-1 >= right and self.data[smallest] <= self.data[right]:
            # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
            smallest = right

        if smallest != i:
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[smallest], self.data[i] = self.data[i], self.data[smallest]

            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(smallest)      

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data


# 힙 정렬의 시간복잡도 : O(N*logN)
def heapsort(unsorted):
    H = MaxHeap()
    # 1. 정렬되지 않은 원소들을 아무 순서로나 최대 힙에 삽입 : O(logN)
    for item in unsorted: 
        H.insert(item)
    sorted = []
     # 2. 삽입이 끝나면, 힙이 비게 될 때까지 하나씩 삭제 : O(logN)
    d = H.remove()
    while d:
        sorted.append(d)
        d = H.remove()
    return sorted # 3. 원소들이 삭제된 순서가 원소들의 정렬 순서



h = MaxHeap()
h.insert(30)
h.insert(8)
h.insert(14)
h.insert(21)
h.insert(27)
h.insert(1)
h.insert(19)
h.insert(5)
h.insert(24)
print(h.data)
h.remove()
print(h.data)