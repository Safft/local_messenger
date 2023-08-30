import socket
from PyQt6.QtCore import QObject, pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6.QtCore import QThread

from PyQt6 import QtWidgets
from ui.receiver import Wind_ui
import sys


class Server_thread_func(QObject):

    signal_msg = Signal()

    def __init__(self):
        super().__init__(self)
        self.client_ip = '10.157.10.6'
        self.server_ip = '10.157.10.7'
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (self.server_ip, 12345)
        self.server_socket.bind(self.server_address)

        self.server_socket.listen(1)
        print('Waiting for a client to connect...')

        self.client_socket, self.client_address = self.server_socket.accept()
        print('Client connected: ', self.client_address)

        #self.connect_signal()

    def connect_signal(self):
        pass


    def run_server(self):
        try:
            while True:
                message = self.client_socket.recv(1024).decode()
                print('server')
                if message:
                    # нужно дописать получение и отпарвку
                    self.mes_from_client = message
                    print('От клиента: ', message)

                    #message_2 = input('Enter a message: ')

                    self.client_socket.sendall(self.message2client.encode())
        except KeyboardInterrupt:
            pass

        self.client_socket.close()
        self.server_socket.close()

    @Slot(str)
    def update_send_mes(self, data):
        self.message2client = data

    def run(self):
        flag = True
        while flag:
            self.run_server()