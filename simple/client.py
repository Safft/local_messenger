import socket
from PyQt6.QtCore import QObject, pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6 import QtWidgets
from ui.receiver import Wind_ui
import sys

class Client_wind():

    def __init__(self):
        super().__init__()
        self.wind_client = Wind_ui()
        self.client_ip = '10.157.10.6'
        self.server_ip = '10.157.10.7'
        self.run_client()

    def run_client(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.server_ip, 12345)
        client_socket.connect(server_address)

        try:
            while True:
                message = input('Enter a message: ')
                client_socket.sendall(message.encode())

                response = client_socket.recv(1024).decode()
                print('От сервера:', response)
        except KeyboardInterrupt:
            pass

        client_socket.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Client_wind()
    controller.wind_client.show()
    sys.exit(app.exec())