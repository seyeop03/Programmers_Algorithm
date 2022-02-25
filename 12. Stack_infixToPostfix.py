import string

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

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    
    for c in S:
        if c in string.ascii_uppercase:
            answer += c
        elif c == '(':
            opStack.push(c)
        elif c == ')':
            while opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop()
        elif c in prec:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[c]:
                answer += opStack.pop()
            opStack.push(c)      
            
    while not opStack.isEmpty():
        answer += opStack.pop()
    
    return answer