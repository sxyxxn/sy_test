# ifelse.py
# 선택한 영역 주석처리 : ctrl + /
# score = int(input("점수를 입력:"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ",grade)

value = 5
while value > 0:
    print(value)
    value -= 1

d = {"apple":100, "orange":200}
for item in d.items():
    print(item)

lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item > 5:
        break
    print("Item:{0}".format(item))

print("---continue---")
for item in lst:
    if item % 2 == 0:
        continue
    print("Item:{0}".format(item))