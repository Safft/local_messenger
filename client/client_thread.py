import socket
from PyQt6.QtCore import QObject, pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6.QtCore import QThread

class Client_thread(QObject):



    def __init__(self):
        super().__init__()
        self.resp_mes = None
        self.message = None
        self.client_ip = '10.157.10.6'
        self.server_ip = '10.157.10.7'
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (self.server_ip, 12345)
        self.client_socket.connect(self.server_address)


    def run(self):
        try:
            while True:
                # нужно дописать получение и отпарвку
                # message = input('Enter a message: ')
                print(111)
                if self.message is not None:
                    self.client_socket.sendall(self.message.encode())

                response = self.client_socket.recv(1024).decode()

                self.update_resp_mes(response)

                print('От сервера:', response)
                print(222)
        except KeyboardInterrupt:
            pass

        self.client_socket.close()

    @Slot(str)
    def update_send_mes(self, data):
        self.message = data

    def update_resp_mes(self, data):
        self.resp_mes = data

    #def run(self):
        # flag = True
        # while flag:
        #     self.run_client()

