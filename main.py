from PyQt6 import QtWidgets
import sys

from mvc.controller import Packages_controller

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # who_is = "Client"
    while True:
        try:
            who_is = input('Введите кто вы: "Client" или "Server"\n')
            if who_is == 'Client' or who_is == 'Server':
                break
            if who_is != 'Client' or who_is != 'Server':
                print("Не правильно.\nПопробуйте написать без ошибок")
        except:
            print("НЕ правильно")
    controller = Packages_controller(who_is)
    controller.wind.setWindowTitle(who_is)
    controller.wind.show()
    sys.exit(app.exec())
