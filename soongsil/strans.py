sentence = input("문자열을 입력하시오 : ")
table = {"alphas" : 0, "digits" : 0, "spaces" : 0, "dots": 0, "lowercase": 0, "uppercase": 0}
for i in sentence:
    if i.isalpha():
        if i.isupper():
            table["uppercase"] += 1
        elif i.islower():
            table["lowercase"] += 1
        table["alphas"] += 1
    elif i.isdigit():
        table["digits"] += 1
    elif i.isspace():
        table["spaces"] += 1
    elif i == ".":
        table["dots"] += 1
print(table)