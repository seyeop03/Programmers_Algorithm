# 지금까지는 A+B와 같이 각 피연산자가 하나의 문자로 구성되어 수식을 문자열 형태로 보아도 무방했으나, ex) "A+B"
# 현실에서는 120+34와 같은 형식으로 많이 쓰이므로
# 120같은 피연산자를 하나의 수로 보기위해 리스트를 사용했다. ex) [120, '+', 34]와 같이 ,,,
# 결과적으로 중위표현식을 후위표현식으로 바꾸는 코드또한 달라져야한다.

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

# 3 + 7 따위의 수식을 [3, '+', 7]로 만들기
def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens

# 중위표현식(3+7)을 후위표현식(37+)로 바꾸기
def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for t in tokenList:
        if type(t) == int:
            postfixList.append(t)
        elif t == '(':
            opStack.push(t)
        elif t == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        elif t in prec:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[t]:
                postfixList.append(opStack.pop())
            opStack.push(t)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList

# 후위표현식(37+) 계산
def postfixEval(tokenList):
    opStack = ArrayStack()

    for token in tokenList:
        if type(token) == int:
            opStack.push(token)
        else:
            if token == '+':
                opStack.push(opStack.pop() + opStack.pop())
            elif token == '-':
                opStack.push(-opStack.pop() + opStack.pop())             
            elif token == '*':
                opStack.push(opStack.pop() * opStack.pop())
            elif token == '/':
                opStack.push(1/opStack.pop() * opStack.pop())
    return opStack.pop()


tokens = splitTokens('(11 + 34) * 4')
postfix = infixToPostfix(tokens)
val = postfixEval(postfix)

print(postfix)
print(val)