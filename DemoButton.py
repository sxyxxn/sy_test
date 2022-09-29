# DemoButton.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# QMain이 마더, DemoWin가 자식
class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI() # 초기화 시 아래의 setupUI() 부름

    def setupUI(self):
        btn1 = QPushButton("닫기", self) # 버튼 생성
        btn1.move(20, 20) # 좌측상단부터 (x,y)만큼 들어가서 버튼 생성
        btn1.clicked.connect(QCoreApplication.instance().quit) # 시그널 + 슬롯 메서드 (실행하던것 종료(quit)시킴)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoWindow()
    demoWindow.show()
    app.exec_() 