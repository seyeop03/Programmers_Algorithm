###################QuickSort##################
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        # Partition
        l = [x for x in arr[1:] if x <= pivot]
        g = [x for x in arr[1:] if x > pivot]         
        return quickSort(l) + [pivot] + quickSort(g)

arr = list(map(int, input().split()))

print(quickSort(arr))
##################LinkedList###################
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, val):
        self.head = ListNode(val)

    def add(self, val):
        curr = self.head
        while curr and curr.val < val:
            prev = curr
            curr = curr.next
        newNode = ListNode(val, curr)
        if curr == self.head:
            self.head = newNode
        else:
            prev.next = newNode

    def print_list(self):
        curr = self.head
        while curr.next:
            print(curr.val, end=" ")
            curr = curr.next
        print(curr.val)


nums = list(map(int, input().split()))
l = LinkedList(nums[0])

for i in nums[1:]:
    l.add(i)
l.print_list()
############플로이드 워셜############
INF = int(1e9)
num_node = int(input())
num_edge = int(input())

dp = [[INF]*(num_node+1) for _ in range(num_node+1)]

for i in range(1, num_node+1):
    dp[i][i] = 0

for _ in range(num_edge):
    x, y, cost = map(int, input())
    dp[x][y] = cost

for k in range(1, num_node+1):
    for x in range(1, num_node+1):
        for y in range(1, num_node+1):
            dp[x][y] = min(dp[x][y], dp[x][k]+dp[k][y])
for x in range(1, num_node+1):
    for y in range(1, num_node+1):
        if dp[x][y] == INF:
            print("INF")
        else:
            print(dp[x][y], end=' ')
    print()
#############프림############
import heapq
V,E = map(int, input().split())
Edge_list = [[] for _ in range(V+1)]
visited = [False]*(V+1)
heap = [[0, 1]]
answer, cnt = 0, 0

for _ in range(E):
    s, e, x = map(int, input().split())
    Edge_list[s].append([x, e])
    Edge_list[e].append([x, s])

while heap:
    if cnt == V:
        break
    x, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += x
        cnt += 1
        for i in Edge_list[s]:
            heapq.heappush(heap, i)

print(answer)
#################TSP##################
n = int(input())
INF = int(1e9)
dp = [[INF]*(1 << n) for _ in range(n)]

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, visited):
    if visited == (1 << n) - 1:
        if graph[x][0]:
            return graph[x][0]
        else:
            return INF
    if dp[x][visited] != INF:
        return dp[x][visited]
    for i in range(1, n):
        if not graph[x][i]:
            continue
        if visited & (1 << i):
            continue
        dp[x][visited] = min(dp[x][visited], dfs(i, visited|(1<<i))+graph[x][i])
    return dp[x][visited]


print(dfs(0,1))
############################연쇄행렬 최소곱셈###################################
import sys

def MatrixChainOrder(p, n):
    # p=[1,2,3,4], n=4
    DP = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n): # DP[1][1] = DP[2][2] = DP[3][3] = 0
        DP[i][i] = 0
        
    # L은 체인의 길이, i는 행, j는 열
    for L in range(2, n): # L --> 2, 3  ∵ n=4이므로
        for i in range(1, n-L + 1): # L이2일때 i --> 1,2 and L이 3일때 i --> 1
            j = i + L-1
            DP[i][j] = sys.maxsize # int 최대값을 초기화
            for k in range(i, j):
                # 비용 계산
                q = DP[i][k] + DP[k+1][j] + p[i-1]*p[k]*p[j]
                # 동적 계획을 위해 미리 저장
                if q < DP[i][j]:
                    DP[i][j] = q
                    
    return DP[1][n-1]

arr = list(map(int, input().split()))
size = len(arr)

print("최소 연산 수: " + str(MatrixChainOrder(arr, size)))
############################크루스칼 알고리즘###################################
# 특정 원소가 속한 집합을 찾기(cycle닫혔는지 확인)
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기(cycle형성이 안되면 최소신장트리에 경로를 넣어준다.)
def union_parent(parent, a, b):
    R_a = find_parent(parent, a)
    R_b = find_parent(parent, b)
    if R_a < R_b:
        parent[R_b] = R_a
    else:
        parent[R_a] = R_b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기      
v, e = map(int, input().split()) # 정점(vertex), 간선(edge)
parent = [i for i in range(v+1)] # 부모 테이블 초기화 , 부모 테이블상에서, 부모를 자기 자신으로 초기화
# 모든 간선을 담을 리스트, 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플 첫번째 인자를 비용으로 설정
    edges.append((cost, a, b)) # 간선ab, 노드a, 노드b
    
edges.sort() # 간선 값 오름차순 정렬
# edges = [(7,3,4), (13,4,7), (23,4,6), (23,6,7), (29,1,2), (34,2,6), (35,2,3), (53,5,6), (75,1,5)]

# 간선을 하나씩 확인하면서,
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        
print(result)

######################################## 사분면##########################################
# 어떤 분면으로 가는 알고리즘이다. 맨처음 3사분면가고, 그다음 3안의 4사분면 그다음 3안의 4안의 1사분면...
def find(n1, n2, m1, m2, idx):
    if idx == len(number): # 입력 사분면의 수와 인덱스가 일치하면 return
        return n1, m1

    if number[idx] == '1': # 입력이 1사분면일 때
        return find(n1, (n1+n2)//2, (m1+m2)//2, m2, idx+1) # 1 사분면 조각내기
    elif number[idx] == '2': # 입력이 2사분면일 때
        return find(n1, (n1+n2)//2, m1, (m1+m2)//2, idx+1) # 2 사분면 조각내기 
    elif number[idx] == '3': # 입력이 3사분면일 때
        return find((n1+n2)//2, n2, m1, (m1+m2)//2, idx+1) # 3 사분면 조각내기
    elif number[idx] == '4': # 입력이 4사분면일 때
        return find((n1+n2)//2, n2, (m1+m2)//2, m2, idx+1) # 4 사분면 조각내기

def check(n1, n2, m1, m2):
    global answer
    if len(answer) == int(d): # 입력 자릿수와 answer에 누적된 글자수(341)와 같으면 return
        return answer
    
    if (n1 <= nx < (n1+n2)//2) and ((m1+m2)//2 <= ny < m2): # 새로운 좌표가 1사분면에 해당
        answer += '1'
        return check(n1, (n1 + n2) // 2, (m1 + m2) // 2, m2) # 1사분면 조각내기
    elif (n1 <= nx < (n1+n2)//2) and (m1 <= ny < (m1+m2)//2): # 새로운 좌표가 2사분면에 해당
        answer += '2'
        return check(n1, (n1 + n2) // 2, m1, (m1 + m2) // 2) # 2사분면 조각내기 
    elif ((n1+n2)//2 <= nx < n2) and (m1 <= ny < (m1+m2)//2): # 새로운 좌표가 3사분면에 해당
        answer += '3'
        return check((n1 + n2) // 2, n2, m1, (m1 + m2) // 2) # 3사분면 조각내기
    elif ((n1+n2)//2 <= nx < n2) and ((m1+m2)//2 <= ny < m2): # 새로운 좌표가 4사분면에 해당
        answer += '4'
        return check((n1 + n2) // 2, n2, (m1 + m2) // 2, m2) # 4사분면 조각내기
        
d, number = input().split()      # 3 341 , (4^3, pos)
x, y = map(int, input().split()) # 2 1   , (ㅈ만한 사각형 size로 x->2, y->1만큼 움직인다.)

n, m = 2**int(d), 2**int(d)      # 사분면이 몇개의 조각으로 이루어지는지 계산 n, m = 2^3, 2^3

dx, dy = find(0, n, 0, m, 0)     # 사분면 조각의 좌표( 6, 3 )
nx, ny = (-1*y) + dx, x + dy     # 새로운 사분면 조각의 좌표
answer = ''

if 0 <= nx < n and 0 <= ny < m:
    print(int(check(0, n, 0, m)))
else:
    print(-1)    
#####################################BST###################################################
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst(nums):
    length = len(nums)
    if not length:
        return None
    mid = length // 2
    return TreeNode(nums[mid], bst(nums[:mid]), bst(nums[mid+1:]))

arr = list(map(int, input().split()))
tree = bst(arr)

def preorder(node):
    print(node.val, end=" ")
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

preorder(tree)
