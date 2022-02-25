# 사실 파이썬에는 from pythonds.basic.queue import Queue으로 이미 만들어진 라이브러리가 구현되어있다.

# 큐의 활용:
# 자료를 생성하는 작업과 그 자료를 이용하는 작업이
# 비동기적으로(asynchronously) 일어나는 경우
class ArrayQueue:

    def __init__(self):
        self.data = [] # 빈 큐를 초기화


    def size(self):
        return len(self.data) # 큐의 크기를 리턴

    def isEmpty(self):
        return self.size() == 0 # 큐가 비어있는지 판단 

    def enqueue(self, item):
        self.data.append(item) # 데이터 원소를 추가
    
    def dequeue(self):
        return self.data.pop(0) # 맨앞 데이터 원소를 삭제(리턴)
    
    def peek(self):
        return self.data[0] # 큐의 맨 앞 원소 반환

    
