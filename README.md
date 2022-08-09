# LinkedList
&nbsp;
## 0x01. insertAt ( LinkedList ) vs insertAt ( <u>Dummy LinkedList</u> )

### insertAt ( LinkedList )
- **1**에 추가할때 그놈을 헤드로..
- **나머지인덱스**는 prev노드를 먼저 찾고, 
  - <newNode가 prev노드 next를 가리키게>하고, <prev노드 next는 newNode를 가리키게>
- (+추가) 맨끝+1 인덱스에 노드집어넣을경우 그 노드를 tail로 조정

<br>

### insertAt ( <u>Dummy LinkedList</u> )

- 그냥 prev노드 찾아서 insertAfter을 호출

#### insertAfter ( <u>Dummy LinkedList</u> )

- <newNode가 prev노드 next를 가리키게>하고, <prev노드 next는 newNode를 가리키게>

&nbsp;&nbsp;&nbsp;


## 0x02. popAt ( LinkedList ) vs popAt ( Dummy LinkedList )

### popAt ( LinkedList )
- **1**을 꺼낼때 현재헤드의 next를(None을) 새롭게 head로..
  - 단, 데이터가 0개가 되므로 tail도 None으로 조정

- **나머지 인덱스** 꺼낼때는 prev찾고, prev의 next가 curr.next를 가리키도록!
  - 단, 맨 마지막놈을 꺼낼땐 tail도 하나 전껄로 변경

<br>

### popAt ( Dummy LinkedList )

- 그냥 prev찾아서 popAfter 호출

#### popAfter ( Dummy LInkedList )

- prev의 next가 curr.next를 가리키도록!
  - 단, prev의 next가 None이면(<u>끝놈을 삭제했을 경우</u>), <u>tail을 prev</u>로 조정

<br>

---

<br>

# Stack

> 연산자 우선순위가 높다: 상대적으로 스택 꼭대기 근방에 있다.

## <기본>
infix -> postfix
1. 문자는 그냥 후위표현식에 적는다.
2. 첫번째 연산자는 스택에 넣는다.
3. 그다음 연산자 만나면 스택꼭대기에 있는 놈과 우선순위 비교 후
    - 스택에 있는 연산자가 더 높으면 pop해서 계산한다.
    - 아니면 스택에 push한다.

- **[중위]** A * B + C
- **[후위]** A B * C +
 
<br />

- **[중위]** A + B * C
- **[후위]** A B C * +

<br />

- **[중위]** A + B + C
- **[후위]** A B + C +

## <괄호의 처리>

> 괄호는 스택 내 `구분선`이다
  
1. `(` 는 스택에 push 
   - ∵ `(` 가 들어가기 전에는 우선순위가 가장 높으므로 무조건 push
  > 단, ( 가 들어가는 순간 우선순위가 가장 낮음
2. `)` 를 만나면 `(` 가 나올 때까지 pop

- **[중위]** (A + B) * C
- **[후위]** A B + C *

<br />

- **[중위]** A * (B + C)
- **[후위]** A B C + *

<br />

- **[중위]** (A + B) * (C + D)
- **[후위]** A B + C D + *

<br />

- **[중위]** A * (B + C)
- **[후위]** A B C + *

<br />

- **[중위]** (A + (B - C)) * D
- **[후위]** A B C - + D *

<br />

- **[중위]** A * (B - (C + D))
- **[후위]** A B C D + - *

<br />

---

<br />

# 힙(Heap) 이란?

## 0x01. 힙(Heap)의 정의

- **이진 트리**의 한 종류 (이진 힙 - binary heap)
  - 루트 (root) 노드가 언제나 최댓값 or 최솟값을 가짐
    - 최대 힙 (max heap), 최소 힙 (min heap)
    - ex) 최대 힙 : 부모는 무조건 자식보다 큼
    - ex) 최소 힙 : 부모는 무조건 자식보다 작음
  - But, `left subtree`와 `right subtree`는 `부모보다 작다는 것` 외에는 관계 X
    - 따라서 이진 탐색 트리보다는 느슨한 정렬(탐색, 순회에 적합하지 X)
- **완전 이진 트리**여야 함

> 완전 이진 트리: leaf 노드가 아니라면 다 채워져 있는 트리
>
> 이진 탐색 트리: left subtree < 자기자신 < right subtree

## 0x02. 최대 힙의 ADT
- __`__init__()`__ : 빈 최대 힙을 생성
- __`insert(item)`__ : 새로운 원소를 삽입
- __`remove()`__ : 최대 원소 (root node)를 반환 (동시에 이 노드를 삭제)



