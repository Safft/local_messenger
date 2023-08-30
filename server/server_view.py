from ui.receiver import Wind_ui
from PyQt6.QtCore import QObject, pyqtSignal as Signal, pyqtSlot as Slot, QThread
import sys
from PyQt6.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6 import QtWidgets
from ui.receiver_des import Ui_Rreceiver


class Server_view(QtWidgets.QMainWindow):

    signal_send = Signal()

    def __init__(self):
        super().__init__()
        self.window = Ui_Rreceiver()
        self.window.setupUi(self)

    @Slot(str)
    def update_label(self, data):
        self.window.label.setText(data)
