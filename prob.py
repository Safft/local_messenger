from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit


class Model:
    def __init__(self):
        self.data = ""

    def update_data(self, new_data):
        self.data = new_data


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.label = QLabel("Data:")
        self.layout.addWidget(self.label)

        self.text_edit = QLineEdit()
        self.layout.addWidget(self.text_edit)

        self.button = QPushButton("Update")
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def get_user_input(self):
        return self.text_edit.text()

    def set_label_text(self, text):
        self.label.setText(f"Data: {text}")


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.button.clicked.connect(self.update_data)

    def update_data(self):
        user_input = self.view.get_user_input()
        self.model.update_data(user_input)
        self.view.set_label_text(self.model.data)


app = QApplication([])

model = Model()
view = View()
controller = Controller(model, view)

main_window = QMainWindow()
main_window.setCentralWidget(view)
main_window.show()

app.exec()

