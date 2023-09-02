from PyQt6.QtCore import QObject, pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6.QtCore import QThread
from client.client_thread import Client_thread
from client.client_view import Client_view
from cryptography.fernet import Fernet



class Packages_controller(QObject):

    signal_send_client = Signal(str)
    signal_send_view = Signal(str)


    def __init__(self):
        super().__init__()
        self.text_from_lbl = None
        self.text_from_txedit = None
        self.cipher_key = b'4BR6r28_0-Xv8T4nLLARqM-b6u4nxhK_lPXj5M62O6Y='
        self.cipher = Fernet(self.cipher_key)
        self.wind = Client_view()
        self.client_thread = Client_thread()
        self.connect_signal()
        self.thread_client = QThread()
        self.wind.window.pushButton.clicked.connect(self.rec_mes)
        self.client_thread.moveToThread(self.thread_client)
        self.thread_client.started.connect(self.client_thread.run)
        self.thread_client.start()

    def rec_mes(self):
        self.text_from_txedit = self.wind.window.textEdit.toPlainText()
        self.text_from_lbl = self.wind.window.label.text()

        encrypted_text = self.cipher.encrypt(self.text_from_txedit.encode())

        self.client_thread.client_socket.sendall(encrypted_text)
        self.signal_send_view.emit(self.text_from_txedit)

        self.wind.window.textEdit.clear()


    def connect_signal(self):
        self.signal_send_view.connect(self.wind.update_label)
        self.client_thread.signal_client.connect(self.wind.update_label)
