import turtle

# 화살표 모양으로 터틀 객체 생성
t = turtle.Turtle()
t.shape("arrow")

# 삼각형 그리기
for i in range(3):
    t.forward(100)   # 선 그리기
    t.left(120)      # 120도 왼쪽으로 회전

# 그리기 종료
turtle.done()