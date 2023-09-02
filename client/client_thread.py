import socket
from PyQt6.QtCore import QObject, pyqtSignal as Signal
from configparser import ConfigParser
from cryptography.fernet import Fernet

class Client_thread(QObject):

    signal_client = Signal(str)

    def __init__(self):
        super().__init__()
        self.config = ConfigParser(allow_no_value=True)
        self.read_ini()
        self.cipher_key = b'4BR6r28_0-Xv8T4nLLARqM-b6u4nxhK_lPXj5M62O6Y='
        self.cipher = Fernet(self.cipher_key)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (self.server_ip, 12345)
        self.client_socket.connect(self.server_address)


    def run(self):
        try:
            while True:
                response = self.client_socket.recv(1024)
                decrypted_text = self.cipher.decrypt(response).decode()
                self.signal_client.emit(decrypted_text)

        except KeyboardInterrupt:
            pass

        self.client_socket.close()

    def read_ini(self):
        self.config.read("settings.ini", encoding="utf-8")
        self.server_ip = str(self.config["Address"]["ip_address"])




