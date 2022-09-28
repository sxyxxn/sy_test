# demoRandom.py
import random
import sys

print( random.random() )
print( random.random() )

lotto = list(range(1,46))
print(lotto)
random.shuffle(lotto)
print(lotto)

print("---샘플링---")
print( random.sample(range(20),10) )
print( random.sample(range(20),10) )
print( random.sample(range(20),10) )

# 파일명 다루기
from os.path import *
print( abspath("python.exe") )
print( basename("c:\\python39\\python.exe") )
print( getsize("c:\\python39\\python.exe") ) # 결과*0.001 KB

# 운영체제 정보
from os import *
print("운영체제:",name)
#system("notepad.exe") # notepad라는 실행파일 실행해라는 의미 > 빈 메모장 열림

# 파일리스트
import glob
print( glob.glob("c:\\work\\*.py") ) # 리스트로 출력
result = glob.glob("c:\\work\\*.*")
for item in result:
    print(item) # 하나씩 출력

