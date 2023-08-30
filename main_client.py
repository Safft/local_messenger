from PyQt6 import QtWidgets
import sys

from client.client_controller import Packages_controller

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Packages_controller()
    controller.wind.setWindowTitle('Клиент')
    controller.wind.show()
    sys.exit(app.exec())
