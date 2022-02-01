### 리스트에서 원소 찾아내기
import string

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

# import string

# def solution(new_id):
#     new_id = new_id.lower()
#     new_id = list(new_id)
#     for i, e in enumerate(new_id):
#         if(e not in string.digits and \
#           e not in string.ascii_lowercase and \
#            e != '_' and e != '-' and e != '.'       
#           ):
#             new_id.remove(e)
        
#     print(new_id)
#     answer = ''
#     return answer