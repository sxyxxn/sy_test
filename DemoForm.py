# DemoForm.py
# DemoForm.ui(화면단) + Demoform.py(로직단)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 화면 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]

# 클래스 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")

# 직접 모듈을 실행한 경우(진입점, 자바에서 main()함수 )
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()
