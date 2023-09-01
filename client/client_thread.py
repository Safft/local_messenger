import socket
from PyQt6.QtCore import QObject, pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6.QtCore import QThread

class Client_thread(QObject):
    signal_client = Signal(str)


    def __init__(self):
        super().__init__()
        self.resp_mes = None
        self.flag = False
        self.message = '333'

        self.client_ip = '10.157.10.6'
        self.server_ip = '10.157.10.7'
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (self.server_ip, 12345)
        self.client_socket.connect(self.server_address)


    def run(self):
        try:
            while True:
                # нужно дописать получение и отпарвку
                # self.message = input('Enter a message: ')

                response = self.client_socket.recv(1024).decode()

                self.update_resp_mes(response)

                print('От сервера:', response)

                self.signal_client.emit(response)

        except KeyboardInterrupt:
            pass

        self.client_socket.close()

    def update_resp_mes(self, data):
        self.resp_mes = data


