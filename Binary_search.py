def solution(L, x):
    first = 0
    last = len(L)-1
    while first <= last:
        middle = (first + last) // 2
        if L[middle] == x:
            answer = middle
            break
        elif L[middle] > x:
            last = middle - 1
        elif L[middle] < x:
            first = middle + 1
    if first > last:
        answer = -1
    return answer