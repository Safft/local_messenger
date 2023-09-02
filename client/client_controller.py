from PyQt6.QtCore import QObject, pyqtSignal as Signal, pyqtSlot as Slot
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
        self.wind.window.pushButton.clicked.connect(self.rec_mes)
        self.client_thread.moveToThread(self.thread_client)
        self.thread_client.started.connect(self.client_thread.run)
        self.thread_client.start()

    def rec_mes(self):
        self.text_from_txedit = self.wind.window.textEdit.toPlainText()
        self.text_from_lbl = self.wind.window.label.text()
        text = self.text_from_lbl + "\n" + "Клиент: " + self.text_from_txedit
        self.client_thread.client_socket.sendall(text.encode())
        self.signal_send_view.emit(text)

    @Slot(str)
    def send_to_server(self, data):
        self.wind.window.label.setText(data)


    def connect_signal(self):
        self.signal_send_view.connect(self.wind.update_label)
        self.client_thread.signal_client.connect(self.send_to_server)
