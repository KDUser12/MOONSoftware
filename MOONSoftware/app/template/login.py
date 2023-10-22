from PyQt5.QtWidgets import QMainWindow, QFrame, QLabel, QTextEdit, QPushButton
from app.template.register import RegisterTemplate


# noinspection PyUnresolvedReferences
class LoginTemplate(QMainWindow):
    def __init__(self):
        super().__init__()

        self.registerWindow = None
        self.setWindowTitle("MOONSoftware - Login")
        self.setFixedSize(400, 550)
        self.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #25272F, stop:1 #0E111D);")
        self.initUI()

    def initUI(self):
        icon = QFrame(self)
        icon.setStyleSheet("background-color : #A0A0A0; border-radius : 50px;")
        icon.setGeometry(150, 50, 100, 100)

        title = QLabel("Email", self)
        title.setStyleSheet("background: transparent; color: #AEAEAE; font-size: 15px; font-family: Arial; font-weight"
                            ":300;")
        title.setGeometry(50, 200, 100, 26)

        textBox = QTextEdit(self)
        textBox.setGeometry(90, 200, 277, 26)
        textBox.setPlaceholderText("Email address")
        textBox.setStyleSheet("background-color: transparent; border: 0; width: 100%; color: #808080; font-size:"
                              "15px; font-family: Arial; font-weight: 300; word-wrap: break-word")

        separator = QFrame(self)
        separator.setStyleSheet("background-color: #363636")
        separator.setGeometry(50, 225, 300, 1)

        title = QLabel("Password", self)
        title.setStyleSheet("background: transparent; color: #AEAEAE; font-size: 15px; font-family: Arial; font-weight:"
                            "300;")
        title.setGeometry(50, 230, 100, 26)

        textBox = QTextEdit(self)
        textBox.setGeometry(120, 230, 250, 26)
        textBox.setPlaceholderText("Password")
        textBox.setStyleSheet("background-color: transparent; border: 0; width: 100%; color: #808080; font-size: "
                              "15px; font-family: Arial; font-weight: 300; word-wrap: break-word")

        separator = QFrame(self)
        separator.setStyleSheet("background-color: #363636;")
        separator.setGeometry(50, 255, 300, 1)

        label = QPushButton("FORGOT PASSWORD ?", self)
        label.setStyleSheet("background: transparent; color: #AEAEAE; font-size: 15; font-family: Arial;"
                            "background-color: transparent;")
        label.setGeometry(220, 265, 150, 25)

        button = QPushButton("LOGIN", self)
        button.setStyleSheet("background-color: transparent; border-radius: 17; border: 1px solid #AEAEAE;"
                             "color: #AEAEAE; font-size: 15; font-weight: 600; font-family: Arial; word-wrap: "
                             "break-word;")
        button.setGeometry(50, 300, 300, 35)

        button = QPushButton("SIGN UP", self)
        button.setStyleSheet("background-color: #263354; border-radius : 17; color: #AEAEAE; font-size: 15;"
                             "font-weight : 600; font-family: Arial; word-wrap: break-word;")
        button.setGeometry(50, 350, 300, 35)
        button.clicked.connect(self.register)

    def register(self):
        self.hide()
        self.registerWindow = RegisterTemplate(self)
        self.registerWindow.show()
