import turtle

# 거북이 모양으로 터틀 객체 생성
t = turtle.Turtle()
t.shape("turtle")

# 선 색상 설정
t.pencolor("blue")

# 내부를 채우기 위한 색 설정
t.fillcolor("green")

# 삼각형 그리기
for i in range(3):
    t.forward(100)   # 선 그리기
    t.left(120)      # 120도 왼쪽으로 회전

# 내부 채우기 종료
t.end_fill()

# 그리기 종료
turtle.done()