# 사실 파이썬에는 from pythonds.basic.stack import Stack으로 이미 만들어진 라이브러리가 구현되어있다.

### 스택을 Python리스트와 메서드들을 이용하여 구현

class ArrayStack:

	def __init__(self):
		self.data = []

	def size(self):
		return len(self.data)

	def isEmpty(self):
		return self.size() == 0

	def push(self, item):
		self.data.append(item)

	def pop(self):
		return self.data.pop()

	def peek(self):
		return self.data[-1]