from PyQt5.QtWidgets import QWidget, QFrame, QLabel, QTextEdit, QPushButton


# noinspection PyUnresolvedReferences
class RegisterTemplate(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.setWindowTitle("MOONSoftware - Register")
        self.setFixedSize(400, 550)
        self.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #25272F, stop:1 #0E111D);")
        self.initUI()

    def initUI(self):
        icon = QFrame(self)
        icon.setStyleSheet("background-color: #A0A0A0; border-radius: 50px;")
        icon.setGeometry(150, 50, 100, 100)

        title = QLabel("Username", self)
        title.setStyleSheet("background: transparent; color: #AEAEAE; font-size: 15px; font-family: Arial; font-weight:"
                            "300;")
        title.setGeometry(50, 200, 100, 26)

        textBox = QTextEdit(self)
        textBox.setGeometry(120, 200, 245, 26)
        textBox.setPlaceholderText("Username")
        textBox.setStyleSheet("background-color: transparent; border: 0; width: 100%; color: #808080; font-size:"
                              "15px; font-family: Arial; font-weight: 300; word-wrap: break-word")

        separator = QFrame(self)
        separator.setStyleSheet("background-color: #363636")
        separator.setGeometry(50, 225, 300, 1)

        title = QLabel("Email", self)
        title.setStyleSheet("background: transparent; color: #AEAEAE; font-size: 15px; font-family: Arial; font-weight:"
                            "300;")
        title.setGeometry(50, 230, 100, 26)

        textBox = QTextEdit(self)
        textBox.setGeometry(90, 230, 277, 26)
        textBox.setPlaceholderText("Email address")
        textBox.setStyleSheet("background-color: transparent; border: 0; width: 100%; color: #808080; font-size:"
                              "15px; font-family: Arial; font-weight: 300; word-wrap: break-word")

        separator = QFrame(self)
        separator.setStyleSheet("background-color : #363636")
        separator.setGeometry(50, 255, 300, 1)

        title = QLabel("Password", self)
        title.setStyleSheet("background: transparent; color: #AEAEAE; font-size: 15px; font-family: Arial; font-weight:"
                            "300;")
        title.setGeometry(50, 260, 100, 26)

        textBox = QTextEdit(self)
        textBox.setGeometry(120, 260, 250, 26)
        textBox.setPlaceholderText("Password")
        textBox.setStyleSheet("background-color: transparent; border: 0; width: 100%; color: #808080; font-size:"
                              "15px; font-family: Arial; font-weight: 300; word-wrap: break-word")

        separator = QFrame(self)
        separator.setStyleSheet("background-color: #363636;")
        separator.setGeometry(50, 285, 300, 1)

        title = QLabel("Confirm password", self)
        title.setStyleSheet("background: transparent; color: #AEAEAE; font-size: 15px; font-family: Arial; font-weight:"
                            "300;")
        title.setGeometry(50, 290, 125, 26)

        textBox = QTextEdit(self)
        textBox.setGeometry(175, 291, 185, 26)
        textBox.setPlaceholderText("Confirm password")
        textBox.setStyleSheet("background-color: transparent; border: 0; width: 100%; color: #808080; font-size:"
                              "15px; font-family: Arial; font-weight: 300; word-wrap: break-word")

        separator = QFrame(self)
        separator.setStyleSheet("background-color: #363636;")
        separator.setGeometry(50, 315, 300, 1)

        SignUpButton = QPushButton("SIGN UP", self)
        SignUpButton.setStyleSheet(" background-color: transparent; border-radius: 17; border: 1px solid #AEAEAE;"
                                   "color: #AEAEAE; font-size: 15; font-weight: 600; font-family: Arial; word-wrap:"
                                   "break-word;")
        SignUpButton.setGeometry(50, 350, 300, 35)

        signInButton = QPushButton("SIGN IN", self)
        signInButton.setStyleSheet("background-color: #263354; border-radius: 17; color: #AEAEAE; font-size: 15;"
                                   "font-weight: 600; font-family: Arial; word-wrap: break-word;")
        signInButton.setGeometry(50, 400, 300, 35)
        signInButton.clicked.connect(self.login)

    def login(self):
        self.close()
        self.main_window.show()
