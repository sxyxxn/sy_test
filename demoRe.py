# demoRe.py
import re
#print( dir(re) ) # 대문자로 나오는 것들은 상수값

result = re.search("[0-9]*th","  35th") # 숫자 여러개와 th가 포함되어 있는것
# 매칭 오브젝트
print(result)
print(result.group())   # 찾은 것을 문자로 보여줌(?)

# result = re.match("[0-9]*th","  35th")
# print(result)
# print(result.group())

# search는 "  35th" 처럼 빈칸이 있어도 찾지만 match는 빈칸에 대한 명령은 없었으므로 찾지 못함
# (보통 search 사용)
