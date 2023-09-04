from PyQt6.QtCore import pyqtSlot as Slot
from PyQt6 import QtWidgets
from ui.window_design import Ui_Rreceiver


class View(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.window = Ui_Rreceiver()
        self.window.setupUi(self)

    @Slot(str)
    def update_label(self, data):
        self.window.label.setText(self.window.label.text() + "\n" + data)
