import socket
from PyQt6.QtCore import QObject, pyqtSignal as Signal
from configparser import ConfigParser
from cryptography.fernet import Fernet


class Module_thread(QObject):

    signal_msg = Signal(str)

    def __init__(self, who_is):
        super().__init__()
        self.config = ConfigParser(allow_no_value=True)
        self.read_ini()
        self.who_is = who_is
        self.cipher_key = b'4BR6r28_0-Xv8T4nLLARqM-b6u4nxhK_lPXj5M62O6Y='
        self.cipher = Fernet(self.cipher_key)

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (self.server_ip, 12345)

        if self.who_is == 'Client':
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_address = (self.server_ip, 12345)
            self.client_socket.connect(self.server_address)
        else:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_address = (self.server_ip, 12345)
            self.server_socket.bind(self.server_address)

            self.server_socket.listen(1)
            print('Waiting for a client to connect...')

            self.client_socket, self.client_address = self.server_socket.accept()
            print('Client connected: ', self.client_address)



    def run(self):
        try:
            while True:
                message = self.client_socket.recv(1024)
                decrypted_text = self.cipher.decrypt(message).decode()
                if self.who_is == 'Client':
                    self.signal_msg.emit(f'Сервер: {decrypted_text}')
                else:
                    self.signal_msg.emit(f'Клиент: {decrypted_text}')

        except KeyboardInterrupt:
            print("Close")

        if self.who_is == 'Client':
            self.client_socket.close()
        else:
            self.server_socket.close()


    def read_ini(self):
        self.config.read("settings.ini", encoding="utf-8")
        self.server_ip = str(self.config["Address"]["ip_address"])
