import socket
from PyQt6.QtCore import QObject, pyqtSignal as Signal, pyqtSlot as Slot
from configparser import ConfigParser
from cryptography.fernet import Fernet


class Server_thread_func(QObject):

    signal_msg = Signal(str)

    def __init__(self):
        super().__init__()
        self.config = ConfigParser(allow_no_value=True)
        self.read_ini()
        self.cipher_key = b'4BR6r28_0-Xv8T4nLLARqM-b6u4nxhK_lPXj5M62O6Y='
        self.cipher = Fernet(self.cipher_key)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (self.server_ip, 12345)
        self.server_socket.bind(self.server_address)

        self.server_socket.listen(1)
        print('Waiting for a client to connect...')

        self.client_socket, self.client_address = self.server_socket.accept()
        print('Client connected: ', self.client_address)


    def run(self):

        while True:
            message = self.client_socket.recv(1024)
            decrypted_text = self.cipher.decrypt(message).decode()
            self.signal_msg.emit(decrypted_text)



        self.client_socket.close()
        self.server_socket.close()

    def read_ini(self):
        self.config.read("settings.ini", encoding="utf-8")
        self.server_ip = str(self.config["Address"]["ip_address"])
