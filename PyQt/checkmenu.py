import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menu_bar = self.menuBar()
        view_menu = menu_bar.addMenu('View')

        view_stat_act = QAction('View status bar', self, checkable=True)
        view_stat_act.setStatusTip('View status bar')
        view_stat_act.setChecked(True)
        view_stat_act.triggered.connect(self.toggleMenu)

        view_menu.addAction(view_stat_act)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
