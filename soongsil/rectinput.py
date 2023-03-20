# 나만의 터틀 그래픽 만들기

import turtle
t = turtle.Turtle()

###############################################
t.shape("circle")       # 거북이 모양 "circle", "turtle", "square", "arrow" .....
t.color("red")          # 거북이 색상 "red", "green", "blue" .....
t.pencolor("blue")      # 펜 색상 "red", "green", "blue" .....
t.pensize(5)            # 펜 두께
###############################################

# 사용자로부터 사각형의 크기를 받아서 size라는 변수에 저장한다.
# 사각형의 크기는 정수이므로 input()이 반환하는 문자열을 int()를 통하여 정수로 변환하였다.

#size = int(input("사각형의 크기는 얼마로 할까요?"))
size = 100

# 사각형을 다음과 같은 코드로 그린다. 이때 변수 size를 사용하자.
t.forward(size)     # size 만큼 거북이를 전진시킨다.
t.right(90)         # 거북이를 오른쪽으로 90도 회전시킨다.
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)

turtle.done()