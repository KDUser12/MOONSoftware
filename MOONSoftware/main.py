import sys
from PyQt5.QtWidgets import QApplication
from app.template.login import LoginTemplate


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = LoginTemplate()
    root.show()
    sys.exit(app.exec_())
