import sys
from PyQt5.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 1
    label = QLabel(‘HelloWorld’)  # 2
    label.show()  # 3
    sys.exit(app.exec_())  # 4
