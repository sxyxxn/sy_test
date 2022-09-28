# demoFile.py
from cmath import pi


for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---서식지정---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).rjust(3))

print("---서식지정---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(3))

# 서식지정
print("{0:x}".format(10))       # 16진수
print("{0:b}".format(10))       # 2진수
print("{0:e}".format(4/3))      
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(15000000))

# 파일 쓰기(raw string notation) 유니코드 지정
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")  #\n이 나오면 의심할 수 있으니 \\ 두번 사용 or
# r"c:\work\demo.txt"  r을 사용하여 \가 특수문자가 아니라고 알려줌
f.write("첫번째\n두번째\n세번째\n")
f.close()

# 파일 읽기(윈도우는 c:\work // 리눅스, 맥은 /users/kim/desktop)(/를 써도 인식하는듯)
f = open("c:/work/demo.txt", "rt", encoding="utf-8")
# 처음부터 끝까지 하나의 문자열
result = f.read()
print(result)
# 어디쯤 읽고 있어?
print( f.tell() )
# 리셋
f.seek(0)
lst = f.readlines()
#print(lst)
for item in lst:
    print(item, end="") # 기본값은 end="\n". 빈 줄 안나오게 하려고 ""로 씀

print("---한줄씩 처리---")
f.seek(0)
print( f.readline(),end="" )
print( f.readline(),end="" )

f.close()
# print(f.closed)