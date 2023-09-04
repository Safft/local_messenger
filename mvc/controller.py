from PyQt6.QtCore import QObject, pyqtSignal as Signal
from PyQt6.QtCore import QThread
from mvc.module import Module_thread
from mvc.view_gui import View
from cryptography.fernet import Fernet



class Packages_controller(QObject):

    signal_msg = Signal(str)
    signal_send_view = Signal(str)


    def __init__(self, who_is):
        super().__init__()
        self.text_from_txedit = None
        self.who_is = who_is
        self.cipher_key = b'4BR6r28_0-Xv8T4nLLARqM-b6u4nxhK_lPXj5M62O6Y='
        self.cipher = Fernet(self.cipher_key)
        self.wind = View()

        self.thread_work = Module_thread(who_is)

        self.connect_signal()

        self.thread = QThread()
        self.thread_work.moveToThread(self.thread)
        self.thread.started.connect(self.thread_work.run)
        self.thread.start()

    def rec_mes(self):
        self.text_from_txedit = self.wind.window.textEdit.toPlainText()
        encrypted_text = self.cipher.encrypt(self.text_from_txedit.encode())
        self.thread_work.client_socket.sendall(encrypted_text)
        if self.who_is == 'Client':
            self.signal_send_view.emit(f'Клиент: {self.text_from_txedit}')
        else:
            self.signal_send_view.emit(f'Сервер: {self.text_from_txedit}')
        self.wind.window.textEdit.clear()

    def clear_lbl(self):
        self.wind.window.label.clear()


    def connect_signal(self):
        self.signal_send_view.connect(self.wind.update_label)
        self.thread_work.signal_msg.connect(self.wind.update_label)

        self.wind.window.pushButton.clicked.connect(self.rec_mes)
        self.wind.window.del_btn.clicked.connect(self.clear_lbl)
