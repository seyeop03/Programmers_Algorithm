### 정렬된 리스트에 원소 삽입

# 전형적인 python 방식
def solution(L, x):
    for idx, num in enumerate(L):
        if num > x:
            break
    L.insert(idx,x)
    
    return L

# 이진탐색 방식
def solution(L, x):
    first = 0
    last = len(L)-1

    while first <= last:
        middle = (first+last) // 2
        if L[middle] == x:
            L.insert(middle, x)
        elif L[middle] < x:
            first = middle + 1
        elif x < L[middle]:
            last = middle - 1

    L.insert(first, x)    
    answer = L
    return answer
