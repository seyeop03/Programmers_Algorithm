class Node:
    def __init__(self, item=None):
        self.data = item
        self.left = None
        self.right = None
        

class ExpressionTree:
    def __init__(self, postfixExpression):
        self.root = Node() # 루트 생성
        self.postfixExpression = postfixExpression # 후위표기식 생성
        self.buildExpressionTree(self.root)

    # 후위표기식으로 수식트리 구축
    def buildExpressionTree(self, node):
        token = self.postfixExpression[-1]
        self.postfixExpression = self.postfixExpression[:-1]

        # 토큰이 연산자일 때,
        if token in ['+', '-', '*', '/']:
            node.data = token
            node.right = Node()
            node.left = Node()
            self.buildExpressionTree(node.right)
            self.buildExpressionTree(node.left)
        # 토큰이 숫자일 때,
        else:
            node.data = token

    # 트리 제거
    def destroyTree(self):
        self.destroy_tree_helper(self.root)
        self.root = None
    
    def destroy_tree_helper(self, node):
        if node == None:
            return

        self.destroy_tree_helper(node.left)
        self.destroy_tree_helper(node.right)
        del node

    # 전위순회
    def preorder(self, node):
        if node == None:
            return

        print(node.data, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
    
    # 중위순회
    def inorder(self, node):
        if node == None:
            return

        self.inorder(node.left)
        print(node.data, end="")
        self.inorder(node.right)
    
    # 후위순회
    def postorder(self, node):
        if node == None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=" ")

    # 후위순회로 계산
    def postorderEval(self, tree):
        if tree == None:
            return 0

        if tree.data in ['+', '-', '*', '/']:
            left = self.postorderEval(tree.left)
            right = self.postorderEval(tree.right)

            if tree.data == '+':
                result = left + right
            elif tree.data == '-':
                result = left - right
            elif tree.data == '*':
                result = left * right
            elif tree.data == '/':
                result = left / right

            return result
        else:
            return float(tree.data)

ET = ExpressionTree('71*52-/')
print(ET.postorderEval(ET.root))

####### 수식트리 #######
# 피연산자: leaf node
# 연산자: root node 또는 branch node
# 1. 중위표기식(infix)을=>후위표기식(postfix)으로 이미 변환시켰다고 가정후, 후위표기식(postfix)을 인자로 받음
# 2. 후위표기식(postfix)을 뒤쪽에서부터 읽음 ex) 12*78-+에서 +부터읽음
# 3. token이 연산자이면, 가지노드
#   3.1. 이 token뒤의 2개 token이 숫자이면, 각각 right/left child node
#   3.2. 이 token뒤의 2개 token에 연산자가 끼어있다면, 
# 4. token이 숫자이면, 잎노드 
# . 후위순회(post order) (left->right->자기자신)

# class Node:
#     def __init__(self, item):
#         self.data = item
#         self.left = None
#         self.right = None

# class ExpressionTree:
#     def __init__(self):
#         self.root = None

#     # 후위표기식으로 수식트리 구축
#     def constructTree(self, postfix): # 71*52-/
#         stack = []
#         for char in postfix:
#             if isinstance(char, int) or char.isdigit():
#                 node = Node(int(char))
#                 stack.append(node)
#             else:
#                 node = Node(char)
#                 right = stack.pop()
#                 left = stack.pop()
#                 node.right = right
#                 node.left = left
#                 stack.append(node)
#         self.root = stack.pop()

#     def evaluate(self):
#         return self.evaluateNode(self.root)

#     def evaluateNode(self, node):
#         if isinstance(node.data, int):
#             return int(node.data)
#         left_val = self.evaluateNode(node.left)
#         right_val = self.evaluateNode(node.right)
#         if node.data == '+':
#             return left_val + right_val
#         elif node.data == '-':
#             return left_val - right_val
#         elif node.data == '*':
#             return left_val * right_val
#         elif node.data == '/':
#             return left_val / right_val

# ET = ExpressionTree()
# ET.constructTree('71*52-/')
# print(ET.evaluate())