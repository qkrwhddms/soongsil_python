# 조건 연산자

x = int(input("첫 번째 수 = "))
y = int(input("두 번째 주 = "))

#max_value = (x if x > y else y)
#min_value = (y if x > y else x)
#print("큰 수 = ", max_value, "작은 수 = ", min_value)


# 조건을 변경하여 위와 같은 결과 출력

if x >= y:
    max_value = x
    min_value = y
else:
    max_value = y
    min_value = x

print("큰 수 = ", max_value, "작은 수 = ", min_value)