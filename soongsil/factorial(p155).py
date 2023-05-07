n = int(input("정수를 입력하시오 : "))
fact = 1
#for i in range(1, n+1) :
for i in range(n, 0, -1) :
            #fact = fact * i
            fact *= i
            print(f"{i} {fact}")
print(n, "!은", fact, "이다.")