# 전역변수
str = "Not Class Member"
class GString:
    def __init__(self):
        # 인스턴스 멤버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        print(str) # 전역변수로 인식. self.str로 변경해서 명시적 코딩 해야함
        print(self.str)

g = GString()
g.set("First Message")
g.print()
