import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtCore import Qt


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        pix = QPixmap(20, 20)
        pix.fill(Qt.lightGray)
        exit_act = QAction(QIcon(), '&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip("Exit application")
        exit_act.triggered.connect(qApp.quit)

        self.statusBar()

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_act)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
