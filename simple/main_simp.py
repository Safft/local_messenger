from PyQt6.QtCore import QObject, pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6 import QtWidgets
from ui.simpl_window import Wind_ui

import sys


class Packages_controller(QObject):

    main_signal = Signal(int)

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.wind_1 = Wind_ui()
        self.wind_2 = Wind_ui()
        self.wind_1.setWindowTitle("Первый")
        self.wind_2.setWindowTitle("Второй")
        self.wind_1.signal.connect(self.connect_w1)
        self.wind_2.signal.connect(self.connect_w2)

    @Slot(str)
    def connect_w1(self, data):
        self.text_1 = self.wind_1.ui_rec.label.text()
        self.wind_2.ui_rec.label.setText(self.text_1 + "\n" + "Первый: " + data)
        self.wind_1.ui_rec.label.setText(self.text_1 + "\n" + "Первый: " + data)

        self.wind_1.ui_rec.textEdit.clear()

    @Slot(str)
    def connect_w2(self, data):
        self.text_2 = self.wind_2.ui_rec.label.text()
        self.wind_2.ui_rec.label.setText(self.text_2 + "\n" + "Второй: " + data)
        self.wind_1.ui_rec.label.setText(self.text_2 + "\n" + "Второй: " + data)
        self.wind_2.ui_rec.textEdit.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Packages_controller()
    controller.wind_1.show()
    controller.wind_2.show()
    sys.exit(app.exec())

