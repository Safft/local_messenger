from PyQt6.QtCore import QObject, pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6.QtCore import QThread
from server.server_thread import Server_thread_func
from server.server_view import Server_view
from cryptography.fernet import Fernet


class Packages_controller(QObject):

    signal_send_server = Signal(str)
    signal_send_view = Signal(str)


    def __init__(self):
        super().__init__()
        self.text_from_lbl = None
        self.text_from_txedit = None
        self.cipher_key = b'4BR6r28_0-Xv8T4nLLARqM-b6u4nxhK_lPXj5M62O6Y='
        self.cipher = Fernet(self.cipher_key)
        self.wind = Server_view()
        self.server_thread = Server_thread_func()
        self.connect_signal()
        self.thread = QThread()
        self.server_thread.moveToThread(self.thread)
        self.thread.started.connect(self.server_thread.run)
        self.thread.start()
        self.wind.window.pushButton.clicked.connect(self.rec_mes)

    def rec_mes(self):
        self.text_from_txedit = self.wind.window.textEdit.toPlainText()
        self.signal_send_server.emit(self.text_from_txedit)
        self.text_from_lbl = self.wind.window.label.text()

        encrypted_text = self.cipher.encrypt(self.text_from_txedit.encode())

        self.server_thread.client_socket.sendall(encrypted_text)
        self.signal_send_view.emit(self.text_from_txedit)
        self.wind.window.textEdit.clear()



    def connect_signal(self):
        self.signal_send_view.connect(self.wind.update_label)
        self.server_thread.signal_msg.connect(self.wind.update_label)

