### 리스트에서 원소 찾아내기

def solution(L, x):  
    answer = []
    try:    
        if x not in L: 
            raise ValueError # x가 없으면 ValueError 일으킴
            
        for i in range(len(L)):
            if L[i] == x:
                answer.append(i)
    except Exception:
        answer.append(-1)
    
    return answer