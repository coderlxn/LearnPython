import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        imp_menu = QMenu('Import', self)
        imp_act = QAction('Import mail', self)
        imp_menu.addAction(imp_act)

        new_act = QAction('New', self)

        file_menu.addAction(new_act)
        file_menu.addMenu(imp_menu)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Submenu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
