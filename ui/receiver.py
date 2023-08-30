import sys
from PyQt6.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6 import QtWidgets
from ui.receiver_des import Ui_Rreceiver

class Wind_ui(QtWidgets.QMainWindow):

    signal = Signal(str)
    def __init__(self):
        super(Wind_ui, self).__init__()

        self.ui_rec = Ui_Rreceiver()
        self.ui_rec.setupUi(self)
        self.ui_rec.pushButton.clicked.connect(self.rec_mes)


    def rec_mes(self):
        self.signal.emit(self.ui_rec.textEdit.toPlainText())


    @Slot(int)
    def rec_accept(self, data):
        self.ui_rec.label.setText(str(data))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sender = Wind_ui()
    sender.show()
    sys.exit(app.exec())