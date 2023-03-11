import turtle

# 별 모양으로 터틀 객체 생성
t = turtle.Turtle()
t.shape("turtle")
t.shapesize(2)  # 크기를 2배로 설정

# 내부를 채우기 위한 색 설정
t.fillcolor("yellow")

# 내부를 채우기 시작
t.begin_fill()

# 별 모양 그리기
for i in range(5):
    t.forward(100)   # 선 그리기
    t.right(144)      # 144도 오른쪽으로 회전

# 내부 채우기 종료
t.end_fill()

# 그리기 종료
turtle.done()