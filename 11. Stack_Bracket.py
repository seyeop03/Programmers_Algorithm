# 수식을 왼쪽부터 한글자씩 읽어서
# 여는괄호 (, {, [ 를 만나면 스택에 push
# 닫는괄호 ), }, ] 를 만나면
#    1. 스택이 비어있다면 올바르지 않은 수식
#    2. 스택에서 pop하고 짝이 맞는지 확인
#    3. 닫는괄호가 더이상 없는데도 **스택에 남아있다면** 올바르지 않은 수식
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


def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    S = ArrayStack()
    for c in expr:
        if c in '({[':
             S.push(c)
        elif c in match:
            if S.isEmpty():
                return False
            else:
                t = S.pop()
                if t != match[c]:
                    return False
    return S.isEmpty()

print(solution('{(A+B)*(C+D)+4}*24'))
# 괄호들의 짝이 맞는지 아닌지 확인하는 코드
