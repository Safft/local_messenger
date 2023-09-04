import socket
from PyQt6 import QtWidgets
from simple.simpl_window import Wind_ui
import sys


class Server_wind():

    def __init__(self):
        super().__init__()
        self.wind_server = Wind_ui()
        self.client_ip = '10.157.10.6'
        self.server_ip = '10.157.10.7'
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (self.server_ip, 12345)
        self.server_socket.bind(self.server_address)

        self.server_socket.listen(1)
        print('Waiting for a client to connect...')

        self.client_socket, self.client_address = self.server_socket.accept()
        print('Client connected: ', self.client_address)
        self.run_server()

    def run_server(self):
        try:
            while True:
                message = self.client_socket.recv(1024).decode()
                if message:
                    print('От клиента: ', message)

                    message_2 = input('Enter a message: ')
                    self.client_socket.sendall(message_2.encode())
        except KeyboardInterrupt:
            pass

        self.client_socket.close()
        self.server_socket.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Server_wind()
    controller.wind_server.show()
    sys.exit(app.exec())