from PySide import QtCore, QtGui
from dialog import Ui_Dialog
import sys


class Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        dialog = Ui_Dialog()
        dialog.setupUi(self)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())

