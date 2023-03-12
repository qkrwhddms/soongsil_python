import turtle

# 거북이 모양 입력 받기
while True:
    shape = input('거북이 모양을 입력하세요 ("turtle", "arrow", "circle", "square", "triangle", "classic"): ')
    if shape in ["turtle", "arrow", "circle", "square", "triangle", "classic"]:
        turtle.shape(shape)
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")

# 거북이 색상 입력 받기
while True:
    color = input('거북이 색상을 입력하세요 ("red", "green", "blue", "black", "white", "yellow", "purple"): ')
    if color in ["red", "green", "blue", "black", "white", "yellow", "purple"]:
        turtle.color(color)
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")

# 펜 색상 입력 받기
while True:
    pencolor = input('펜 색상을 입력하세요 ("red", "green", "blue", "black", "white", "yellow", "purple"): ')
    if pencolor in ["red", "green", "blue", "black", "white", "yellow", "purple"]:
        turtle.pencolor(pencolor)
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")

# 펜 두께 입력 받기
while True:
    try:
        pensize = int(input('펜 두께를 입력하세요 (숫자): '))
        turtle.pensize(pensize)
        break
    except ValueError:
        print("잘못된 입력입니다. 다시 입력해주세요.")

# 사각형의 크기 입력 받기
while True:
    try:
        size = int(input('사각형의 크기를 입력하세요 (숫자): '))
        break
    except ValueError:
        print("잘못된 입력입니다. 다시 입력해주세요.")

# 사각형 그리기
for i in range(4):
    turtle.forward(size)
    turtle.left(90)

turtle.done()