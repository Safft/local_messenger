from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Rreceiver(object):
    def setupUi(self, Rreceiver):
        Rreceiver.setObjectName("Rreceiver")
        Rreceiver.resize(550, 558)
        self.centralwidget = QtWidgets.QWidget(parent=Rreceiver)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 528, 265))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        Rreceiver.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Rreceiver)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 22))
        self.menubar.setObjectName("menubar")
        Rreceiver.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Rreceiver)
        self.statusbar.setObjectName("statusbar")
        Rreceiver.setStatusBar(self.statusbar)

        self.retranslateUi(Rreceiver)
        QtCore.QMetaObject.connectSlotsByName(Rreceiver)

    def retranslateUi(self, Rreceiver):
        _translate = QtCore.QCoreApplication.translate
        Rreceiver.setWindowTitle(_translate("Rreceiver", "Receiver"))
        self.label.setText(_translate("Rreceiver", "Начни"))
        self.textEdit.setHtml(_translate("Rreceiver", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"></span></p></body></html>"))
        self.pushButton.setText(_translate("Rreceiver", "отправить"))
