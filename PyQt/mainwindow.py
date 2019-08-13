import sys
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    d = QtWidgets.QDialog()
    if d.exec() == QtWidgets.QDialog.Rejected:
        sys.exit(0)

    w = QtWidgets.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle("Hello PyQt")
    w.show()
    sys.exit(app.exec_())
