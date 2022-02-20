# LinkedList

## insertAt ( <span style="color: blue">LinkedList</span> )

- **1**에 추가할때 그놈을 헤드로..
- **나머지인덱스**는 prev노드를 먼저 찾고, 
  - <newNode가 prev노드 next를 가리키게>하고, <prev노드 next는 newNode를 가리키게>
- (+추가) 맨끝+1 인덱스에 노드집어넣을경우 그 노드를 tail로 조정

## insertAt ( <span style="color: red">Dummy LinkedList</span> )

- 그냥 prev노드 찾아서 insertAfter을 호출

## insertAfter ( <span style="color: red">Dummy LinkedList</span> )

- <newNode가 prev노드 next를 가리키게>하고, <prev노드 next는 newNode를 가리키게>

&nbsp;&nbsp;

## popAt ( LinkedList )

- **1**을 꺼낼때 현재헤드의 next를(None을) 새롭게 head로..
  - 단, 데이터가 0개가 되므로 tail도 None으로 조정

- **나머지 인덱스** 꺼낼때는 prev찾고, prev의 next가 curr.next를 가리키도록!
  - 단, 맨 마지막놈을 꺼낼땐 tail도 하나 전껄로 변경

## popAt ( Dummy LinkedList )

- 그냥 prev찾아서 popAfter 호출

## popAfter ( Dummy LInkedList )

- prev의 next가 curr.next를 가리키도록!
  - 단, prev의 next가 None이면(<u>끝놈을 삭제했을 경우</u>), <u>tail을 prev</u>로 조정
