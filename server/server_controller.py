from PyQt6.QtCore import QObject, pyqtSignal as Signal
from PyQt6.QtCore import QThread
from server.server_thread import Server_thread_func
from server.server_view import Server_view



class Packages_controller(QObject):

    signal_send_server = Signal(str)
    signal_send_view = Signal(str)


    def __init__(self):
        super().__init__()
        self.text_from_lbl = None
        self.text_from_txedit = None
        self.wind = Server_view()
        self.server_thread = Server_thread_func()
        self.thread = QThread()
        self.connect_signal()
        self.wind.window.pushButton.clicked.connect(self.rec_mes)

    def rec_mes(self):
        self.text_from_txedit = self.wind.window.textEdit.toPlainText()
        self.signal_send_server.emit(self.text_from_txedit)
        self.text_from_lbl = self.wind.window.label.text()
        text = self.text_from_lbl + "\n" + "Сервер: " + self.text_from_txedit
        self.signal_send_view.emit(text)

    def connect_signal(self):
        self.signal_send_server.connect(self.server_thread.update_send_mes)
        self.signal_send_view.connect(self.wind.update_label)