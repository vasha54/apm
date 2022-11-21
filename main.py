import sys

from PyQt5.QtWidgets import (
    QApplication
)

from PyQt5.QtGui import (
    QIcon
)
from view.app import App
from view.resource import resource

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = App()
    win.showMaximized()
    win.setWindowIcon(QIcon(":/img/falta.png"))
    sys.exit(app.exec())