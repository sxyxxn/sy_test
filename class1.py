# class1.py
# 1)클래스를 정의
class Person:
    # 초기화 메서드
    def __init__(self):
        # 인스턴스 멤버변수 초기화
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

# 2)인스턴스 생성
p1 = Person()

# 3)메서드 호출
p1.print()