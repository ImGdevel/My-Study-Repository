import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,  QDesktopWidget, QHBoxLayout
from PyQt5.QtGui import QIcon, QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QPoint

class MyTitleBar(QWidget):

    def __init__(self, parent):
        super(MyTitleBar, self).__init__()
        self.parent = parent
        print(self.parent.width())
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.title = QLabel("My Own Bar")

        btn_size = 35

        self.btn_close = QPushButton("x")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setFixedSize(btn_size,btn_size)
        self.btn_close.setStyleSheet("""
            background-color: #ff5555;
            color: #f8f8f2;
            font-weight: bold;
            padding: 5px;
        """)

        self.btn_min = QPushButton("-")
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_min.setFixedSize(btn_size, btn_size)
        self.btn_min.setStyleSheet("""
            background-color: #282a36;
            color: #f8f8f2;
            font-weight: bold;
            padding: 5px;
        """)

        self.title.setFixedHeight(35)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_min)
        self.layout.addWidget(self.btn_close)

        self.title.setStyleSheet("""
            background-color: #282a36;
            color: #f8f8f2;
        """)
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(MyTitleBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_close_clicked(self):
        self.parent.close()

    def btn_min_clicked(self):
        self.parent.showMinimized()



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Real-time video filtering program')
        self.setFixedSize(1024, 768)         # 윈도우의 크기를 1024x768으로 고정
        self.center()                       # 윈도우 크기를 가운데에 위치

        self.layout  = QVBoxLayout()
        self.layout.addWidget(MyTitleBar(self))
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.show()


    def center(self):
        qr = self.frameGeometry()           # 프레임 위치
        cp = QDesktopWidget().availableGeometry().center()  #사용자 화면의 가운데 반환
        qr.moveCenter(cp)                   # 창의 위치를 화면 정가운데로 이동
        self.move(qr.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())