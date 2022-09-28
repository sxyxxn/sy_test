# try1.py
# 함수 정의
def divide(a,b):
    return a/b
# 호출
#result = divide(5,0)
#print("결과:{0}".format(result))
# 에러 처리 하지 않으면 ZeroDivisionError: division by zero

# 에러 처리
try:
    # 호출
    result = divide(5,0)
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("숫자여야 연산이 됩니다.")
else: 
    print("결과:{0}".format(result))
finally:
    print("무조건 실행")


print("---전체 코드 종료---")