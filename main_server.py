from PyQt6 import QtWidgets
import sys

from controller.controller import Packages_controller

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    who_is = "Server"

    controller = Packages_controller(who_is)
    controller.wind.setWindowTitle(who_is)
    controller.wind.show()
    sys.exit(app.exec())
