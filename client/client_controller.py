from PyQt6.QtCore import QObject, pyqtSignal as Signal
from PyQt6.QtCore import QThread
from client.client_thread import Client_thread
from client.client_view import Client_view



class Packages_controller(QObject):

    signal_send_client = Signal(str)
    signal_send_view = Signal(str)


    def __init__(self):
        super().__init__()
        self.text_from_lbl = None
        self.text_from_txedit = None
        self.wind = Client_view()
        self.client_thread = Client_thread()
        self.connect_signal()
        self.thread_client = QThread()
        self.client_thread.moveToThread(self.thread_client)
        self.thread_client.started.connect(self.client_thread.run)
        self.thread_client.start()
        self.wind.window.pushButton.clicked.connect(self.rec_mes)

    def rec_mes(self):
        self.text_from_txedit = self.wind.window.textEdit.toPlainText()
        self.signal_send_client.emit(self.text_from_txedit)
        self.text_from_lbl = self.wind.window.label.text()
        text = self.text_from_lbl + "\n" + "Клиент: " + self.text_from_txedit
        self.signal_send_view.emit(text)

    def connect_signal(self):
        self.signal_send_client.connect(self.client_thread.update_send_mes)
        self.signal_send_view.connect(self.wind.update_label)
